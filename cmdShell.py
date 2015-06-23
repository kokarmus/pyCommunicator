#!/usr/bin/python

import re

class CCmdShell:
    def __init__(self):
        self.cmds={'::help':'\t\tdisplay all avaible commands.', '::clear':'\t\tclear your console.', '::quit':'\t\tclose communicator'}
        self.__regExp='::\S+'
        self.__pattern=re.compile(self.__regExp)
    
    def shellCmd(self, cmd):
        if not self.__pattern.match(cmd):
            return 0
        if cmd=='::help':
            print('::Aviable commands are:\n')
            for command, description in self.cmds.iteritems():
                print(command+description)
            return -1
        elif cmd=='::clear':
            print(chr(27) + '[2J')
            return -1
        elif cmd=='::quit':
            return 1
        else:
            print('::Unknown command.')
            return -1
