#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from calculator import Count
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        print('test case start')

    def tearDown(self):
        print('test case end')

class TestAdd(MyTest):
        
    def test_add(self):
        j = Count(2, 3)
        # j = Count(2, 6)
        self.assertEqual(j.add(), 5)

    def test_add_2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)      

class TestSub(MyTest):

    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub_2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)      

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestAdd("test_add"))
    # suite.addTest(TestAdd("test_add_2"))
    # suite.addTest(TestSub("test_sub"))
    # suite.addTest(TestSub("test_sub_2"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
