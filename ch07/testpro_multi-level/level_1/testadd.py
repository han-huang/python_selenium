#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
from calculator import Count

class TestAdd(unittest.TestCase):

    def setUp(self):
        print('test add start')
        
    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add_2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)      
    
    def tearDown(self):
        print('test add end')

if __name__ == '__main__':
    unittest.main()
