# -*- coding: utf-8 -*-
try:
    aa = "例外測試"
    print(aa)
except Exception as e:
    print(e)
finally:
    print("不管是否例外 我都會被執行")
