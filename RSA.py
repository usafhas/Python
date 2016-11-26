# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 14:13:55 2015

@author: Heath
"""

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random


def genKey():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator) #generate pub and priv key
    return key

def exportKey():
    key = genKey()
    with open('privkey', 'w') as priv:
        priv.write(key.exportKey())
    
    with open('pubkey', 'w') as pub:
        pub.write(key.publickey().exportKey())

def importKey():
    with open('privkey', 'rb') as priv:
        imprivkey = RSA.importKey(priv.read())
    with open('pubkey', 'rb') as pub:
        impubkey = RSA.importKey(pub.read())
    print imprivkey.exportKey()
    print impubkey.publickey().exportKey()