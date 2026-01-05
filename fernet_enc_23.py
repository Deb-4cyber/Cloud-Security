#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import AES
import base64
from cryptography.hazmat.primitives import padding
import PyPDF2
from cryptography.fernet import Fernet
from additional import read_file2
from additional import padder_fnc

def fernet_enc_23(file_enc):
    
    inp = file_enc
    key = Fernet.generate_key()
    print("Your key is")
    print(key)
    f = Fernet(key)
    print('Before Decryption:')
    print(inp[:50])
    file_enc_bytes=inp
    token = f.encrypt(file_enc_bytes)
    print('Encrypted File:')
    print(token[:50])
    ans=token
    
    return token,key

