#!/usr/bin/python

import platform

class CSound:
    def __init__(self):
        pass
    
    @staticmethod
    def play():
        if platform.system()=='Linux':
            import os
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.17, 256))
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.15, 512))
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.12, 768))
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.15, 512))
        elif platform.system()=='Windows':
            #windows sound
            pass
        else:
            print('Unknow OS.')
