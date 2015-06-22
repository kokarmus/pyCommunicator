#!/usr/bin/python

#interface for crypto

class IMessageCipher:
    def encryptMsg(self, msg):
        raise NotImplementedError('Subclasses must override '+self.__name__+'(msg).')
    
    def decryptMsg(self, msg):
        raise NotImplementedError('Subclasses must override '+self.__name__+'(msg).')
    
    def getCipherInfo(self):
        raise NotImplementedError('Subclasses must override '+self.__name__+'().')
