#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

# The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way)
# multiprocessing.Pipe([duplex])
# Returns a pair (conn1, conn2) of Connection objects representing the ends of a pipe.
# https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Pipe   
    
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()
