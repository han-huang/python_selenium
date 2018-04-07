#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        print('test start')
        
    def test_case(self):
        a = "hello"
        # a = "hi"
        b = "hello world"
        self.assertIn(a, b, msg="a is not in b!")

    def tearDown(self):
        print('test end')

if __name__ == '__main__':
    unittest.main()
