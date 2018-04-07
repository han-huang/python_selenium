#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://blog.gtwang.org/programming/python-with-context-manager-tutorial/
# http://linbo.github.io/2013/01/08/python-with
# http://icodding.blogspot.tw/2016/05/python-with-as.html
		
class Sample:

    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print("type: %s" % type)
        print("value: %s" % value)
        print("trace: %s" % trace)

    def do_something(self):
        bar = 1/0
        return bar + 10

def main():
    with Sample() as sample:
        sample.do_something()

if __name__ == '__main__':
    main()

	
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch07>python with_example_02.py
# type: <class 'ZeroDivisionError'>
# value: division by zero
# trace: <traceback object at 0x00000213983EDA08>
# Traceback (most recent call last):
  # File "with_example_02.py", line 27, in <module>
    # main()
  # File "with_example_02.py", line 24, in main
    # sample.do_something()
  # File "with_example_02.py", line 19, in do_something
    # bar = 1/0
# ZeroDivisionError: division by zero

# 實際上，在with後面的程式碼塊拋出任何異常時，__exit__() 方法被執行。
# 正如例子所示，異常拋出時，與之關聯的type，value和stack trace傳給 __exit__() 方法，
# 因此拋出的ZeroDivisionError異常被列印出來了。
# 開發庫時，清理資源，關閉文件等等操作，都可以放在 __exit__ 方法當中。	