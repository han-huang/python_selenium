#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import gmtime, strftime, localtime
import locale, time, sys

# Windows 10 platform
tz1 = strftime("%z", gmtime())
print('gmtime()', gmtime())
print(tz1) # +0800
tz2 = strftime("%z", localtime())
print('localtime()', localtime())
print(tz2) # +0800
print()

tz3 = strftime("%Z", localtime())
print(tz3)
# https://segmentfault.com/a/1190000007598639
# 當在shell裡啟動python repl(交互器)時,默認的環境local設置為'C', 也就是沒有當地語系化設置，
# 這時候可以通過 locale.getdefaultlocale() 來查看shell當前環境的locale設置， 並通過 locale.setlocale(locale.LC_ALL, '') 
# 將python解譯器的locale設置成shell環境的locale
print('locale.getlocale()', locale.getlocale())
print('locale.getdefaultlocale()', locale.getdefaultlocale())
locale.setlocale(locale.LC_ALL, '')
print('locale.getlocale()', locale.getlocale())
tz4 = strftime("%Z", localtime())
print(tz4) # 台北標準時間
print()

# http://bbs.fishc.com/thread-76584-1-1.html
# >>> [bytes([ord(c) for c in s]).decode('gbk') for s in time.tzname ]
# ['中国标准时间', '中国标准时间']
tz5 = time.tzname
print(tz5)
tz6 = [bytes([ord(c) for c in s]).decode('big5') for s in time.tzname]
print(tz6) # ['台北標準時間', '台北日光節約時間']
print()
print('sys.stdout.encoding', sys.stdout.encoding) # sys.stdout.encoding utf-8
print('sys.getdefaultencoding()', sys.getdefaultencoding()) # sys.stdout.encoding utf-8
print()

# https://docs.python.org/3/library/functions.html#ord
# ord(c)
# Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. 
# For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().
print(ord('a')) # 97
print(chr(97)) # a
print()
print(ord('€')) # 8364
print(chr(8364)) # €
print()
# https://r12a.github.io/app-conversion/
print(ord('\u6642')) # 26178
print(ord('時')) # 26178
print(chr(26178)) # 時
data_utf8 = b'\xE6\x99\x82' # https://r12a.github.io/app-conversion/  時 UTF-8 code units E6 99 82
print("data_utf8.decode('utf_8')",data_utf8.decode('utf_8')) # data_utf8.decode('utf_8') 時
print("data_utf8.decode('utf_8').encode('utf_8')",data_utf8.decode('utf_8').encode('utf_8')) # data_utf8.decode('utf_8').encode('utf_8') b'\xe6\x99\x82'

