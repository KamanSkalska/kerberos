from Client.Client_functions import derive_key_from_password,encrypt_message
from .models import Message
import random, string





def ticket_and_key_message_generator(message_content,password):
    KDC_password = "jZ3/vu`!U=T*?Wh't%CdNVh'/bG4pm5#tXB{N=<?y+2r"
    KDC_hashed = derive_key_from_password(KDC_password)
    session_key=session_key_generator()
    key_encrypted=encrypt_message(session_key,password)
    new_msg_content=encrypt_message(message_content+", "+session_key,KDC_hashed)
    new_msg=Message(session_key=key_encrypted,content=new_msg_content)
    return new_msg

def session_key_generator():
    session_key = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
    print("Klucz sesji został wygenerowany\n----------------------------------------")
    return session_key
