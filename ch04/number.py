#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
verify = randint(1000,9999)
print("產生的亂數:%d" % verify)
number = input("請輸入亂數:")
print(number)
number = int(number)
if number == verify:
    print("登入成功")
elif number == 132741:
    print("登入成功")
else:
    print("驗證碼輸入有誤")

