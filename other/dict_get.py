#!/usr/bin/env python3
# -*- coding: utf-8 -*-
dict_driver = {"edge": print("edge"), 
               "chrome": print("chrome"),
               "opera": "opera_browser",
               "ff": print("ff")}
driver_str = dict_driver.get("opera", None)
print(driver_str)
print()

def f(x):
    return {
        'a': 1,
        'b': 2,
        'c': print("called")
    }.get(x, 9) 

print(f("a"))



Python 沒有 switch case - dynamic dispatch via getattr or dict.get

http://chestmd.blogspot.tw/2013/06/python-switch-case.html

http://code.activestate.com/recipes/410692/



Replacements for switch statement in Python?

https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python


You could use a dictionary:

def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]



If you'd like defaults you could use the dictionary get(key[, default]) method:

def f(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)    # 9 is default if x not found






# https://stackoverflow.com/questions/46701063/why-doesnt-python-have-switch-case


# There is literally a section in the docs to answer this. See below:

# Why isn’t there a switch or case statement in Python?

# TL;DR: existing alternatives (dynamic dispatch via getattr or dict.get, if/elif chains) cover all the use cases just fine.




# https://docs.python.org/3/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python

# Why isn’t there a switch or case statement in Python?

# You can do this easily enough with a sequence of if... elif... elif... else. There have been some proposals for switch statement syntax, but there is no consensus (yet) on whether and how to do range tests. See PEP 275 for complete details and the current status.

# For cases where you need to choose from a very large number of possibilities, you can create a dictionary mapping case values to functions to call. For example:

# def function_1(...):
    # ...

# functions = {'a': function_1,
             # 'b': function_2,
             # 'c': self.method_1, ...}

# func = functions[value]
# func()

# For calling methods on objects, you can simplify yet further by using the getattr() built-in to retrieve methods with a particular name:

# def visit_a(self, ...):
    # ...
# ...

# def dispatch(self, value):
    # method_name = 'visit_' + str(value)
    # method = getattr(self, method_name)
    # method()
# It’s suggested that you use a prefix for the method names, such as visit_ in this example. Without such a prefix, if values are coming from an untrusted source, an attacker would be able to call any method on your object.





# https://docs.python.org/3/library/functions.html#getattr

# getattr(object, name[, default])

# Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. 

# For example, getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.
