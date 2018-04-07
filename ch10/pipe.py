#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
import multiprocessing

def proc1(pipe):
    pipe.send('hello')
    print('proc1 rec:',pipe.recv())

def proc2(pipe):
    print('proc2 rec:',pipe.recv())
    pipe.send('hello, too')

def main():
	# The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way)
	# multiprocessing.Pipe([duplex])
	# Returns a pair (conn1, conn2) of Connection objects representing the ends of a pipe.
	# https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Pipe
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))
    p1.start()
    p2.start()
    # p1.join()
    # p2.join()

if __name__ == '__main__':
    main()
