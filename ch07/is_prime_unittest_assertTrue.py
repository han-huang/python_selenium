#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from count import is_prime
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        print('test start')
        
    def test_case(self):
        self.assertTrue(is_prime(7), msg="Is not prime!")
        # self.assertTrue(is_prime(8), msg="Is not prime!")

    def tearDown(self):
        print('test end')

if __name__ == '__main__':
    unittest.main()
