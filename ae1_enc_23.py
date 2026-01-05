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

def ae1_enc_23(file_enc):
    
    inp =file_enc
    model='CTR'
    backend=default_backend()
    #print('Select desired mode of operation:')
    #print('CBC,CTR, OFB or CFB. In case of invalid choice, CFB will be taken by default')
    #mode1=input()
    #print('Enter desired key length in bits')
    key_length=32
    key=os.urandom(key_length)
    print('Here is your key')
    print(key)
    
    iv=os.urandom(16)
    iv=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    pad_obj= padding.PKCS7(128).padder()
    #nonce=os.urandom(16)
    #cipher = AES.new(key, AES.MODE_CBC)
    # AES MODE:
    
    #if mode1=='CBC':
    #   cipher=Cipher(algorithms.AES(key),modes.CBC(iv),backend=backend)
    #elif mode1=='CTR':
     #   cipher=Cipher(algorithms.AES(key),modes.CTR(iv),backend=backend)
    #elif mode1=='OFB':
    #    cipher=Cipher(algorithms.AES(key),modes.OFB(iv),backend=backend)
    #else:
     #   cipher=Cipher(algorithms.AES(key),modes.CFB(iv),backend=backend)
    
    #ciphertext, tag = cipher.encrypt_and_digest(iv)
    print(inp)
    cipher=Cipher(algorithms.AES(key),modes.CTR(iv),backend=backend)
    encryptor=cipher.encryptor()
    #print(encryptor)
    plaintext=inp #used while testing
    #print(encoded_string)
    print(pad_obj)
    
   # padded_plaintext1 = pad_obj.update('contentttttttttttttttttt:'.encode())
   # print(padded_plaintext1)
  #  print(pad_obj)
  #  padded_plaintext = pad_obj.update(inp.encode())
  #  print(padded_plaintext)
    
    padded_plaintext = padder_fnc(inp,16)
    
    print('Plaintext:')
    print(padded_plaintext[:])
    print(padded_plaintext.decode())
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    #print(plaintext)
    print('Ciphertext:')
    print(ciphertext[:50])
    print('Here is your key for decryption:')
    print(key)
    decryptor = cipher.decryptor()
    #print(decryptor)
    d=decryptor.update(ciphertext) + decryptor.finalize()
    print('After Decryption:')
    print(d[:50])
    return ciphertext,key

