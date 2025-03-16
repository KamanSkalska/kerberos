# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.primitives import hashes
# from django import middleware
#
# from KDC.models import Message
# import hashlib
#
# class AS_process:
#     def __init__(self,get_response):
#         self.get_response=get_response
#
#
#     # def __call__(self,request):
#     #     message_list=["weron456","349528374957dnfiuw34yhit53","99:00493:34850:0909"] #list
#     #     message=' '.join(message_list)
#     #     response=self.get_response(request)
#     #     password="Haslo123!"
#     #     hashed=derive_key_from_password(password)
#     #     print("My hashesd password is:", hashed)
#     #     encrypted_message=encrypt_message(message,hashed)
#     #     decrytped_messgae=decrypt_message(encrypted_message,hashed)
#     #     print("Odszyfrowana wiadomość: ", decrytped_messgae)
#     #     print("Wiadomość zaszyfrowana: ",encrypted_message)
#     #     response = self.get_response(request)
#     #
#     #     # You can add middleware logic here after the view is called
#     #     latest_message = Message.objects.latest('id')
#     #     message_content = latest_message.content if latest_message else None
#     #     request.latest_message = message_content
#     #     return response
#
#     def process_template_response(self,request,response):
#         response.context_data['website_url']="https:///codewithstein.com"
#         return response
#
# # class CheckRole:
# #     def __init__(self,get_response):
# #         self.get_response=get_response
# #
# #     def process_request(self, get_request):
# #         if request.
#
