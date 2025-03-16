from django.db import models
from django.utils import timezone


class Client_credentials(models.Model):
    login=models.CharField(max_length=30, unique=True)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.login

class Message(models.Model):
    type=models.CharField(max_length=10, default=timezone.now())
    content = models.TextField()

    def __str__(self):
        return self.content

class Ticket(models.Model):
    expire_date=models.DateTimeField
    content=models.TextField

    def __str__(self):
        return self.content