from django.db import models
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import hashlib

from django.utils import timezone

from Client.models import Ticket


#user credentials which are needed for database
class User(models.Model):
    login=models.CharField(unique=True,max_length=30)
    password=models.BinaryField(max_length=100)
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    has_ticket=models.BooleanField(default=False)
    #role=models.enums.Enum("Worker", "Guest", default="Guest")
    def __str__(self):
        return self.login


class Message(models.Model):
    type = models.CharField(max_length=10, default=timezone.now())
    content = models.BinaryField(max_length=200)
    session_key=models.BinaryField(max_length=100)
    def __str__(self):
        return self.content

    class Meta:
        get_latest_by = 'id'

# class SessionKeys(models.Model):
#     key = models.TextField(max_length=40)
#

