#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime

def music():
    # print('listen to music %s' % ctime())
    print('%-20s %s' % ('listen to music', ctime()))
    sleep(2)

def movie():
    # print('watch movie %s' % ctime())
    print('%-20s %s' % ('watch movie', ctime()))
    sleep(5)
    
if __name__ == '__main__':
    music()
    movie()
    # print('at the end %s' % ctime())
    print('%-20s %s' % ('at the end', ctime()))
