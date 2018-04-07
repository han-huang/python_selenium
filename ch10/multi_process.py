#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
import multiprocessing

def player(item, s):
    for i in range(2):
        print('%-20s %-50s %s' % ('playing', item, ctime()))
        sleep(s)

# class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
# args=() -> tuple -> need ","
# https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process
def run_processes():
    dicts = {"U2 - I Still Haven't Found What I'm Looking For":2,
             "molly's game":3,
             "The Avengers":5}
    files = range(len(dicts))
    processes = []
    for f, s in dicts.items():
        t = multiprocessing.Process(target=player, args=(f, s))
        processes.append(t)

    for i in files:
        processes[i].start()
        # processes[i].join() # do not put here, or it can not be multi-process
    for i in files:
        processes[i].join()
    # join([timeout])
    # If the optional argument timeout is None (the default), the method blocks until the process whose join() method is called terminates. 
    # If timeout is a positive number, it blocks at most timeout seconds. Note that the method returns None if its process terminates or 
    # if the method times out. Check the process’s exitcode to determine if it terminated.

if __name__ == '__main__':
    run_processes()
    print('%-70s  %s' % ('at the end', ctime()))
