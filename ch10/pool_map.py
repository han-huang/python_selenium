#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool(processes=3) # 定義CPU核數量為3
    res = pool.map(job, range(10))
    print(res)

# https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/5-pool/
# class multiprocessing.pool.Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])
# https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool
if __name__ == '__main__':
    multicore()
