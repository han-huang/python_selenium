#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = 257
print('id(a) %s', id(a))
b = 257
print('id(b) %s', id(b))

def func():
    c = 257
    print('id(c) %s', id(c))
    print(a is c)  # False

print(a is b)  # True

func()

# https://zhuanlan.zhihu.com/p/31169016
# Python 中也是同樣的道理，因為整數是我們經常使用的物件，為了避免重複的創建、回收，乾脆就把那些常用的整數緩存起來，
# 每次需要使用時直接從緩存中拿，而不是重新創建（重新創建的話，肯定是一個全新的物件）。這些整數的範圍是[-5, 256]，
# 當然這個數字範圍是Python之父決定的，你要改，必須重新編譯Python環境。

# 上面代碼是在一個 test.py 檔中，運行時，a和b的id值相同，而c的id值與a不一樣，因為a、b 在同一個代碼塊，屬於模組層級別，
# 而 c 是在函數裡面，屬於區域變數，他們不屬於同一代碼塊中，因此函數裡面的 257 這個物件時會重新創建，而創建 b 的時候，
# 發現同級代碼塊中有個257的值了，就重用了這個物件。



# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\other>python
# Python 3.6.3 |Anaconda, Inc.| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> a = 256
# >>> print('id(a) %s', id(a))
# id(a) %s 1443528832
# >>> b = 256
# >>> print('id(b) %s', id(b))
# id(b) %s 1443528832
# >>> print(a is b)
# True
# >>> a = 257
# >>> print('id(a) %s', id(a))
# id(a) %s 2201278459632
# >>> b = 257
# >>> print('id(b) %s', id(b))
# id(b) %s 2201309056816
# >>> print(a is b)
# False
# >>> a = 257
# >>> print('id(a) %s', id(a))
# id(a) %s 2201310382800
# >>> b = 257
# >>> print('id(b) %s', id(b))
# id(b) %s 2201278456944
# >>> print(a is b)
# False
# >>> a = 257
# >>> print('id(a) %s', id(a))
# id(a) %s 2201278459632
# >>> b = 257
# >>> print('id(b) %s', id(b))
# id(b) %s 2201310381232
# >>> print(a is b)
# False
# >>> a = 257
# >>> print('id(a) %s', id(a))
# id(a) %s 2201309056816
# >>> b = 257
# >>> print('id(b) %s', id(b))
# id(b) %s 2201278456944
# >>> print(a is b)
# False
# >>> a = 256
# >>> print('id(a) %s', id(a))
# id(a) %s 1443528832
# >>> b = 256
# >>> print('id(b) %s', id(b))
# id(b) %s 1443528832
# >>> print(a is b)
# True
# >>>