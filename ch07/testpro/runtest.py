#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
# import testadd
# import testsub
from testadd import TestAdd
from testsub import TestSub

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))
    suite.addTest(TestAdd("test_add_2"))
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub_2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
