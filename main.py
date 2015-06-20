#!/usr/bin/python

from pyMessanger import CMessanger

try:
    with open('config.conf', 'r') as configFile:
        lines=configFile.readlines()
        clientIp=lines[0].split()[1]
        serverIp=lines[1].split()[1]
        clientPort=int(lines[2].split()[1])
        serverPort=int(lines[3].split()[1])
        #key=raw_input('Insert key:\t')
        key='Sixteen byte key'
except OSError:
    clientIp=raw_input('Insert receiver IPv4:\t')
    serverIp=raw_input('Insert your IPv4:\t')
    clientPort=int(raw_input('Insert receive message communication port:\t'))
    sendPort=int(raw_input('Insert send message communication port:\t'))
    key=raw_input('Insert key:\t')

messanger=CMessanger(clientIp, serverIp, clientPort, serverPort, key)
print('Corpo comunicator is starting...')
messanger.run()
