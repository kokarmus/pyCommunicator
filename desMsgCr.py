#!/usr/bin/python

from des.pyDes import *

class CDESCrypt:
    def __init__(self):
        self.__info='DESCrypt'
        with open('des.conf', 'r') as configFile:
            lines=configFile.readlines()
            self.__key=lines[0].split()[1]
            self.__mode=lines[1].split()[1]
            #self.__iv=lines[2].split()[1]
        self.__cipher=des(self.__key, self.__mode, '\1\3\1\0\1\2\0\1', pad=None, padmode=PAD_PKCS5)
    
    def encryptMsg(self, msg):
        return self.__cipher.encrypt(msg)
    
    def decryptMsg(self, cmsg):
        return self.__cipher.decrypt(cmsg)
    
    def getCipherInfo(self):
        return self.__info

