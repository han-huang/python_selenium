#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import multiprocessing
import time, os

def inputQ(queue):
    # info = str(os.getpid()) + '(put):' + str(time.time())
    info = '%-5s (put): %s' % (str(os.getpid()), str(time.time()))
    queue.put(info)

def outputQ(queue, lock):
    info = queue.get()
    ot = str(time.time())
    lock.acquire()
    # print(str(os.getpid()) + '(get):' + info)
    # print('%-5s (get): %s' % (str(os.getpid()), info))
    print('%-5s (get): %-19s from %s' % (str(os.getpid()), ot, info))
    lock.release()

def main(): 
    record1 = [] # list of input processes
    record2 = [] # list of output processes
    lock = multiprocessing.Lock() # 加鎖，為防止散亂的列印
    queue = multiprocessing.Queue(3)

    #input processes
    for i in range(10):
        process = multiprocessing.Process(target=inputQ, args=(queue,))
        process.start()
        record1.append(process)

    #output processes
    for i in range(10):
        process = multiprocessing.Process(target=outputQ, args=(queue,lock))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()

    queue.close() # 沒有更多的物件進來，關閉queue

    for p in record2:
        p.join()

if __name__ == '__main__':
    main()
