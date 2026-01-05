#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from cryptography.hazmat.primitives import padding
import PyPDF2
from Crypto.Util.Padding import pad
from ae1_enc import ae1_enc
from ae1_enc_23 import ae1_enc_23
from cha2_enc import cha2_enc
from cha2_enc_23 import cha2_enc_23
from fernet_enc import fernet_enc
from fernet_enc_23 import fernet_enc_23



def main():

    c=list()
    kd=list()
    file_enc= 'test.txt' #pathname to  file
    print('How many rounds of encryption do you want to run? 1-3 rounds available')
    rounds=input()
    for i in range(int(rounds)):
        if i ==0:
            print('Round 1 - Do you want to run AES or ChaCha20 encryption? Enter 1 for AES and 2 for ChaCha20 Default Option will be Fernet Cipher')
            choice=input()
            if choice=='1':
                #print('AES')
                c_file,k=ae1_enc(file_enc)
            elif choice=='2':
                #print('Cha')
                c_file,k=cha2_enc(file_enc)
            else:
                #print('Fernet')
                c_file,k=fernet_enc(file_enc)
            c.append(c_file)
            kd.append(k)
        else:
            print('Round 2 - Do you want to run AES or ChaCha20 encryption? Enter 1 for AES and 2 for ChaCha20 Default Option will be Fernet Cipher')
            choice=input()
            if choice=='1':
                #print('AES')
                c_file,k=ae1_enc_23(c_file)
            elif choice=='2':
                #print('Cha')
                c_file,k=cha2_enc_23(c_file)
            else:
                #print('Fernet')
                c_file,k=fernet_enc_23(c_file)
            c.append(c_file)
            kd.append(k)
        print('ecnrypted file and keys:')
        print(c_file,k)

main()
    #print(c_file)
        
                

