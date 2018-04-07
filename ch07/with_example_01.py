#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://blog.gtwang.org/programming/python-with-context-manager-tutorial/
# http://linbo.github.io/2013/01/08/python-with
# http://icodding.blogspot.tw/2016/05/python-with-as.html

# 緊跟with後面的語句被求值後，返回物件的 __enter__() 方法被呼叫，這個方法的返回值將被賦值給as後面的變數。
# 當with後面的程式碼塊全部被執行完之後，將呼叫前面返回物件的 __exit__()方法。

class Sample:

    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        print("In __exit__()")

def get_sample():
    return Sample()

def main():
    with get_sample() as sample:
        print("sample: %s" % sample)

if __name__ == '__main__':
    main()

# output:
# In __enter__()
# sample: Foo
# In __exit__()