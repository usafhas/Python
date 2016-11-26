# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 17:39:56 2015

@author: usafhas
"""

from Crypto.Cipher import DES3
from Crypto import Random

def encrypt(message, key):
    iv = Random.get_random_bytes(8)
    
    des3 = DES3.new(key, DES3.MODE_CFB, iv)
    cipher_text = des3.encrypt(message)
    return cipher_text
    
def decrypt(cipher_text, key):
    des3 = DES3.new(key, DES3.MODE_CFB)
    message = des3.decrypt
    return message