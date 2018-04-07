#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

# The Queue class is a near clone of queue.Queue
# class multiprocessing.Queue([maxsize])
# Returns a process shared queue implemented using a pipe and a few locks/semaphores.
# When a process first puts an item on the queue a feeder thread is started which transfers objects from a buffer into the pipe.
# https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()
