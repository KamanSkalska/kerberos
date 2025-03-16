from json import JSONEncoder

from django.shortcuts import render
from django.template.response import TemplateResponse

from KDC.models import Message, User
from django.http import JsonResponse
from .forms import LoginForm, RegisteringForm
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
from django.contrib import messages
from time import time
import json
from KDC.AuthenticationServer import decrypt_message
from Client.Client_functions import derive_key_from_password,encrypt_message
from KDC.TicketGrantingServer import ticket_and_key_message_generator


def index(request):
    return redirect(reverse('login'))

def service(request):
    if request.method == 'GET':
        print("Yeah mamy dostęp")
        login = request.session.get('login')
        print("login",login)
        user = User.objects.get(login=login)
        print(user.has_ticket)
        if user.has_ticket == True:
            print("Yeah mamy ticket")
            return render(request, "actual_ticket.html")
        else:
            return HttpResponse("Użytkownik nie ma dostępu")
        # TODO sprawdzanie biletu tylko nie wysyłany bilet przez usera tylko przez kdc
    else:
        return TemplateResponse(request, "service.html", {
            'title':'Testing URL'
        })
    return render(request, "actual_ticket.html")

def login_form(request):
    ip_address="10.0.6.1"
    timestamp=str(time())
    request.session.clear()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if(form.is_valid()):
            #getting info
            login=form.cleaned_data['login']
            password=form.cleaned_data['password']
            print("Hasło zostało zahaszhowane przy użyciu SHA-256\n --------------------------------------------")
            hashed=derive_key_from_password(password)
            message = ", ".join([login, ip_address, timestamp])
            new_message=encrypt_message(message,hashed)
            print(f"login: {login} - password: {password} - hashed: {hashed}, ticket: {new_message}")
            print("Wiadomość do serwera została zaszyfrowana\n --------------------------------------------")
            #processing info
            try:
                user = User.objects.get(login=login)
                print(f"user pass: {user.password} - password: {password}, hashed: {hashed}")
                print(user.password,hashed,type(user.password),type(hashed))
                if user.login == login:
                    message_save = Message(content=new_message)
                    message_save.save()
                    request.session['login'] = login
                    request.session['message_id'] = message_save.id
                    request.session['hashed_session_key'] = str(hashed)
                    print("redirecting to main")
                    return redirect(reverse('main'))
            except User.DoesNotExist:
                return render(request, "not_a_user.html")
    else:
        form = LoginForm()
    return render(request, "login.html", {'form': form})  # redirect to login


def registering_form(request):
    if (request.method) == "POST":
        form = RegisteringForm(request.POST)
        if (form.is_valid()):
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            name=form.cleaned_data['name']
            surname=form.cleaned_data['surname']
            print("Hasło zostało zahaszhowane przy użyciu SHA-256\n --------------------------------------------")
            hashed = derive_key_from_password(password)
            print("Hashed type: ",type(hashed))
            new_user = User.objects.create(login=login, password=hashed,name=name,surname=surname)
            new_user.save()
            print("Nowy użytkownik został utworzony\n --------------------------------------------")
            messages.success(request,"You are registered, log in!")
            return render(request, "login.html", {'form': form})
    form = RegisteringForm()
    return render(request, "register.html", {'form': form})

def main_page(request):
    if (request.method)=="GET":
        if type(request.session.get('hashed_session_key')) != type(None):
            login = request.session.get('login')
            hashed_password = request.session.get('hashed_session_key')
            message = Message.objects.get(id=request.session.get('message_id'))
            try:
                user = User.objects.get(login=login)
                if user.login == login and str(user.password) == hashed_password:
                    decrypted_message = decrypt_message(message.content, user.password)
                    print("Decrypted_message:",type(decrypted_message), decrypted_message)
                    print("Autentykacja użytkownika przebiegła pomyslnie \n ----------------------------------")
                    message_received=ticket_and_key_message_generator(decrypted_message,user.password)
                    print("Ticket oraz klucz sesji zostały odebrane")
                    print("Ticket: ",message_received.content, "\n--------------------------------------")
                    print("Klucz sesji: ",message_received.session_key, "\n--------------------------------------")
                    user.has_ticket=True
                    user.save()
                    print("Użytkownik ma dostęp do serwisu \n-----------------------------")
                    return render(request,"main_page.html")
            except User.DoesNotExist:
                return redirect("../login")
        else:
            return redirect("../login")
    else:
        print("Blad logowania - uzytkownik nie istnieje")
    return render(request, "main_page.html")









