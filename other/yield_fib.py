#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://hk.saowen.com/a/e37f3fb7d7a97657c6ed9c782834d93c3cdaeee9d9cb750bbd9b871375b5268a
def fibs(num):
    a = b = 1
    for i in range(num):
        yield a
        a, b = b, a + b # (a, b) = (b, a + b)

print(list(fibs(10))) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(list(fibs(10))[-1]) # 55


# C:\Users\Han\python_book_yehnan\ch06\ch06_fib_gf.py
def fib_gf():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b # (a, b) = (b, a + b)

fib_g = fib_gf()
print([next(fib_g) for _ in range(11)]) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
