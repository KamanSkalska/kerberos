from django import forms
from django.db import models
from .models import User

class LoginForm(forms.Form):
    login=forms.CharField(label="User Login",max_length=30)
    password=forms.CharField(label="User Password",max_length=100,widget=forms.PasswordInput)

class RegisteringForm(forms.Form):
    name=forms.CharField(label="Name",max_length=30)
    surname=forms.CharField(label="Surname",max_length=30)
    login=forms.CharField(label="User Login",max_length=30)
    password=forms.CharField(label="User Password",max_length=100,widget=forms.PasswordInput)

