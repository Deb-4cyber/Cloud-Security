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

def cha2_enc(file_enc):
    inp=''
    inp = read_file2(file_enc)
    backend=default_backend()
    nonceval = os.urandom(16)
    print('nonce')
    nonceval=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    print(nonceval)
    key2=os.urandom(32)
    print('Here is your key')
    print(key2)
   
    algorithm2 = algorithms.ChaCha20(key2,nonceval)
    cipher2= Cipher(algorithm2,mode=None,backend=backend)
    encryptor2 = cipher2.encryptor()
    print('Plaintext:')
    print(inp[:50])
    ciphertext2 = encryptor2.update(inp.encode())+ encryptor2.finalize()
    #print(b"a secret message")
    print('Ciphertext:')
    print(ciphertext2[:50])
    
    return ciphertext2,key2

