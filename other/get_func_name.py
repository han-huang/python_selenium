#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
exec_text = 'sys._getframe().f_code.co_name'

def get_func_name():
    return exec(sys._getframe().f_code.co_name)

def my_function():
    text = sys._getframe().f_code.co_name
    # text = get_func_name()
    return text

def test_func():
    return get_func_name()
    # return print(exec(exec_text))

print(my_function()) # my_function
print(test_func()) # None

# https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string-in-python
# import sys
# this_function_name = sys._getframe().f_code.co_name

