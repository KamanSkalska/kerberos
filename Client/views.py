from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
import requests

def send_message(request):
    message_data = str(["weron456", "349528374957dnfiuw34yhit53", "99:00493:34850:0909"])
    server_url = 'http://localhost:8000/kdc/receive-message/'
    response = requests.post(server_url, data={'message_data': message_data})
    json_resp = response.text
    return JsonResponse({'status': 'success', 'message': 'Message sent successfully.', 'response': json_resp}, safe=False)