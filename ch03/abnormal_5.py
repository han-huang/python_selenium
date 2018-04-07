# -*- coding: utf-8 -*-
try:
    aa = "例外測試"
    print(aa)
except Exception as msg:
    print(msg)
else:
    print("沒有例外")
