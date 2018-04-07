#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime

def music(item, loop):
	for i in range(loop):
		print('%-20s %-50s %s' % ('listen to music', item, ctime()))
		sleep(2)

def movie(item, loop):
	for i in range(loop):
		print('%-20s %-50s %s' % ('watch movie', item, ctime()))
		sleep(1)

if __name__ == '__main__':
    music("U2 - I Still Haven't Found What I'm Looking For", 2)
    movie("molly's game", 2)
    print('%-70s  %s' % ('at the end', ctime()))
