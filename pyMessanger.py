#!/usr/bin/python

import socket
from threading import *
import re, time

from AESMsgCr import CCryptoMessage

class CMessanger:
    def __init__(self, clientIp, serverIp, port, crKey):
        if type(clientIp) and type(serverIp) is not str:
            raise Exception('Receiver and server IPv4 must be a string.')
        if type(port) is not int:
            raise Exception('Port must be integer type.') 
        #if recvPort==sendPort:
        #    raise Exception('Send and receive port must be others.')
        self.__ip4Pattern=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.$')
        res=self.__ip4Pattern.match(clientIp)
        #if not res:
        #    raise Exception('Wrong receiver IPv4 format.')
        res=self.__ip4Pattern.match(serverIp)
        #if not res:
        #    raise Exception('Wrong  server IPv4 format')
        self.__clientIp4=clientIp
        self.__serverIp4=serverIp
        self.__port=port
        self.__crMsg=CCryptoMessage(crKey)
        self.__isClientRun=True
    
    def __del__(self):
        try:
            self.__clientSock
            self.__clientSock.close()
        except Exception as err:
            pass
        
    def __startServer(self):
        self.__serverSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__serverAddress=(self.__serverIp4, self.__port)
        print('SERVER LOG ['+time.strftime('%H:%M:%S')+']: socket was created on port: '+str(self.__port)+'\tand host: '+self.__serverIp4)
        self.__serverSock.bind(self.__serverAddress)        
        self.__serverSock.listen(1)
        print('SERVER LOG ['+time.strftime('%H:%M:%S')+']: listening...')
        while 1:
            if self.__isClientRun==False:
                print('SERVER LOG ['+time.strftime('%H:%M:%S')+']: taking down...')
                return 0
            connection, clientAddress=self.__serverSock.accept()        
            print('SERVER LOG ['+time.strftime('%H:%M:%S')+']: connection established with: '+str(clientAddress))
            try:
                while 1:
                    cmsg=connection.recv(1024)
                    if cmsg:                        
                        print('[MSG FROM '+str(clientAddress)+' ('+time.strftime('%H:%M:%S')+')]:\t'+self.__crMsg.decryptMsg(cmsg))
                    else:
                        break
            finally:
                pass
                connection.close()
    
    def __startClient(self):
        print('CLIENT LOG ['+time.strftime('%H:%M:%S')+']: starting...')
        self.__clientSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('CLIENT LOG ['+time.strftime('%H:%M:%S')+']: socket was created...')
        clientAddress=(self.__clientIp4, self.__port)
        while 1:
            try:
                print('CLIENT LOG ['+time.strftime('%H:%M:%S')+']: try connect with: '+self.__clientIp4+' on port: '+str(self.__port))
                self.__clientSock.connect(clientAddress)
                break
            except:
                print('CLIENT LOG ['+time.strftime('%H:%M:%S')+']: server doesn\'t response. Waiting...')
                time.sleep(2)
        print('CLIENT LOG ['+time.strftime('%H:%M:%S')+']: connected with server.')
        while True:
            msg=raw_input('ME:\t')
            if msg==':q':
                self.__isClientRun=False
                print('CLIENT LOG ['+time.strftime('%H:%M:%S')+']: taking down...')
                self.__clientSock.close()
                print('CLIENT LOG ['+time.strftime('%H:%M:%S')+']: socket  closed.')
                return 0
            emsg=self.__crMsg.encryptMsg(msg)
            try:
                self.__clientSock.send(emsg)
            except Exception as err:
                print(err)
    
    def run(self):
        self.__serverThread=Thread(target = self.__startServer, args = ())
        self.__serverThread.start()
        self.__clientThread=Thread(target = self.__startClient, args = ())
        self.__clientThread.start()
