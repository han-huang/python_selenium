#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys, os
print(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))
from calculator import Count

class TestSub(unittest.TestCase):

    def setUp(self):
        print('test sub start')

    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub_2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)      

    def tearDown(self):
        print('test sub end')

if __name__ == '__main__':
    unittest.main()
