#!/usr/bin/python

#from Crypto.Cipher import AES
#from Crypto import Random
from msgCipher import IMessageCipher

class CCryptoMessage(IMessageCipher):
    def __init__(self, key):
        if type(key) is not str:
            raise Exception('Key must be a string.')
        if len(key) not in (16, 24, 32):
            #AES 128-because key is 16 bytes || (16, 24, 32) bytes keys gaves us (128, 192, 256) AES
            raise Exception('Length of key must be equal 16, 24 or 32')
        self.__key=key
        #self.__iv=Random.new().read(AES.block_size)
        #self.__cipher=AES.new(self.__key, AES.MODE_CFB, self.__iv)
        self.__info='AES:\t'+str(len(self.__key))+' bit'
    
    def encryptMsg(self, msg):
        #return self.__iv+self.__cipher.encrypt(msg)
        return msg
    
    def decryptMsg(self, cmsg):
        #return self.__cipher.decrypt(cmsg)[len(self.__iv):]
        return cmsg
    
    def getCipherInfo(self):
        return self.__info

