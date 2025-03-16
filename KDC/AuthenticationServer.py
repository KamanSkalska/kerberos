from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from KDC.models import Message, User
from KDC.forms import LoginForm
import hashlib

def hash_password_SHA256(password):
    binary_password = b'password'
    hashed = hashlib.sha256()
    hashed.update(binary_password)
    hashed_password = hashed.hexdigest()
    return hashed_password


def derive_key_from_password(password):
    # Using PBKDF2 for key derivation
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 requires a 256-bit key
        salt=b"salty_salt",
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


def encrypt_message(message, key):
    # Using AES encryption in CBC mode
    iv = b'1234567890123456'  # Initialization Vector, should be random and unique for each encryption
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    return ciphertext


def decrypt_message(ciphertext, key):
    # Using AES decryption in CBC mode
    iv = b'1234567890123456'  # Initialization Vector, should match the one used for encryption
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_message.decode()

