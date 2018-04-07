#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
import threading

class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
        print('self.name - %s' % self.name)

    # http://www.runoob.com/python3/python3-multithreading.html
    # 我們可以通過直接從 threading.Thread 繼承創建一個新的子類，並產生實體後調用 start() 方法啟動新執行緒，即它調用了執行緒的 run() 方法    
    def run(self):  
        self.func(*self.args)

def player(item, s):
    for i in range(2):
        print('%-20s %-50s %s' % ('playing', item, ctime()))
        sleep(s)

def run_threads():
    dicts = {"U2 - I Still Haven't Found What I'm Looking For":2,
             "molly's game":3,
             "The Avengers":5}
    files = range(len(dicts))
    threads = []
    for f, s in dicts.items():
        t = threading.Thread(target=player, args=(f, s))
        t = MyThread(player, (f, s), player.__name__)
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

# class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
# args=() -> tuple -> need ","
# https://docs.python.org/3/library/threading.html#threading.Thread

# start()
# Start the thread’s activity.
# It must be called at most once per thread object. It arranges for the object’s run() method to be invoked in a separate thread of control.

# run()
# Method representing the thread’s activity.
# You may override this method in a subclass. The standard run() method invokes the callable object passed to the object’s constructor as the target argument, 
# if any, with sequential and keyword arguments taken from the args and kwargs arguments, respectively.

# http://www.runoob.com/python3/python3-multithreading.html

    
# def movie(item, loop):
    # for i in range(loop):
        # print('%-20s %-50s %s' % ('watch movie', item, ctime()))
        # sleep(1)  