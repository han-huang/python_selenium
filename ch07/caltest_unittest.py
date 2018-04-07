#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from calculator import Count
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        print('test start')
        
    def test_add(self):
        j = Count(2, 3)
        # j = Count(2, 6)
        self.assertEqual(j.add(), 5)

    def tearDown(self):
        print('test end')

if __name__ == '__main__':
    unittest.main()
