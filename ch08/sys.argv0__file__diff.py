#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# http://andylin02.iteye.com/blog/933237

print(__file__)
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.dirname(os.path.abspath(__file__)))

import sys, os
print("script: sys.argv[0] is", repr(sys.argv[0]))
print("script: sys.argv[0] is %s" % sys.argv[0])
print("script: sys.argv[0] is {0}".format(sys.argv[0]))
print("script: __file__ is", repr(__file__))
print("script: cwd is", repr(os.getcwd()))
print()
import whereutils
whereutils.show_where()




