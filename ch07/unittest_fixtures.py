#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

# https://docs.python.org/3/library/unittest.html#class-and-module-fixtures

def setUpModule():
		print("test module start >>>>>")

def tearDownModule():
		print("test module end <<<<<")		
		
class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("test class start ====>")

    @classmethod
    def tearDownClass(cls):
        print("test class end <====")		
		
    def setUp(self):
        print("test case start ---->")

    def test_case(self):
        print("test case 1")

    def test_case_2(self):
        print("test case 2")    

    def tearDown(self):
        print("test case end <----")

if __name__ == '__main__':
    unittest.main()
