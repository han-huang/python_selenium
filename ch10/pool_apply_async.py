#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool() 
    res = pool.map(job, range(10))
    print(res)

    # apply_async()中只能傳遞一個值，它只會放入一個核進行運算，但是傳入值時要注意是可迭代的，
    # 所以在傳入值後需要加逗號, 同時需要用get()方法獲取返回值
    res = pool.apply_async(job, (2,))
    # 用get獲得結果
    print(res.get())
    # 迭代器，i=0時apply一次，i=1時apply一次等等
    # apply_async()只能放入一組參數，並返回一個結果，如果想得到map()的效果需要通過迭代
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    # 從反覆運算器中取出
    print([res.get() for res in multi_res])

# https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/5-pool/
# class multiprocessing.pool.Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])
# https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool
if __name__ == '__main__':
    multicore()
