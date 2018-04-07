#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
def show_where():
    print("show_where: sys.argv[0] is", repr(sys.argv[0]))
    print("show_where: sys.argv[0] is %s" % sys.argv[0])
    print("show_where: sys.argv[0] is {0}".format(sys.argv[0]))
    print("show_where: __file__ is", repr(__file__))
    print("show_where: cwd is", repr(os.getcwd()))

if __name__ == '__main__':
    show_where()

