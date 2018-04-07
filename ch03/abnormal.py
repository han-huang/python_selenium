# -*- coding: utf-8 -*-
# open('abc.txt', 'r')
try:
    open('abc.txt', 'r')
    # print(aa)
except FileNotFoundError:
    print('FileNotFoundError 例外!')
except NameError:
    print('NameError 例外!')
