#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
import threading

def music(item, loop):
    for i in range(loop):
        print('%-20s %-50s %s' % ('listen to music', item, ctime()))
        sleep(2)

def movie(item, loop):
    for i in range(loop):
        print('%-20s %-50s %s' % ('watch movie', item, ctime()))
        sleep(1)

# class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
# args=() -> tuple -> need ","
# https://docs.python.org/3/library/threading.html#threading.Thread
# http://www.runoob.com/python3/python3-multithreading.html
def run_threads():
    threads = []
    t1 = threading.Thread(target=music, args=("U2 - I Still Haven't Found What I'm Looking For", 2))
    threads.append(t1)
    t2 = threading.Thread(target=movie, args=("molly's game", 2))
    threads.append(t2)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    run_threads()
    print('%-70s  %s' % ('at the end', ctime()))
