# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 18:09:28 2015

@author: usafhas
"""
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]


class AESCipher:
    
    def __init__( self, key ):
        self.key = hashlib.sha256(key.encode()).digest()
    
#    def pad(raw):
#        #s = len(raw)
#        mpad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
#        return mpad
#        
#    def unpad(enc):
#        #s = len(enc)
#        encupad = lambda s : s[:-ord(s[len(s)-1:])]
#        return encupad

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ) 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[AES.block_size:] ))
        
  