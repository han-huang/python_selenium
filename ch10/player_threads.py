#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
import threading

def player(item, s):
    for i in range(2):
        print('%-20s %-50s %s' % ('playing', item, ctime()))
        sleep(s)

# def movie(item, loop):
    # for i in range(loop):
        # print('%-20s %-50s %s' % ('watch movie', item, ctime()))
        # sleep(1)

# class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
# args=() -> tuple -> need ","
# https://docs.python.org/3/library/threading.html#threading.Thread
# http://www.runoob.com/python3/python3-multithreading.html
def run_threads():
    dicts = {"U2 - I Still Haven't Found What I'm Looking For":2,
             "molly's game":3,
             "The Avengers":5}
    files = range(len(dicts))
    threads = []
    for f, s in dicts.items():
        t = threading.Thread(target=player, args=(f, s))
        threads.append(t)

    for i in files:
        threads[i].start()
        # threads[i].join() # do not put here, or it can not be multi-thread
    for i in files:
        threads[i].join()
    # join(timeout=None)
    # Wait until the thread terminates. This blocks the calling thread until the thread whose join() method is called terminates – either normally or through an unhandled exception 
    # – or until the optional timeout occurs.

if __name__ == '__main__':
    run_threads()
    print('%-70s  %s' % ('at the end', ctime()))
