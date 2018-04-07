# -*- coding: utf-8 -*-
# open('abc.txt', 'r')
try:
    open('abc.txt', 'r')
except BaseException as msg:
    print(msg) # [Errno 2] No such file or directory: 'abc.txt'

