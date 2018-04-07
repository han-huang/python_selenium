#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

class TestB(unittest.TestCase):

    def setUp(self):
        print('test TestB start')

    def test_1(self):
        print('test TestB test_1')

    def test_cc(self):
        print('test TestB test_cc')

    def test_aa(self):
        print('test TestB test_aa')

    def tearDown(self):
        print('test TestB end')

class TestAdd(unittest.TestCase):

    def setUp(self):
        print('test TestAdd start')
        
    def test_bb(self):
        print('test TestAdd test_bb')  

    def tearDown(self):
        print('test TestAdd end')

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
	# use TestSuite addTest() for test sequence
    suite.addTest(TestB("test_1"))
    suite.addTest(TestB("test_cc"))
    suite.addTest(TestB("test_aa"))
    suite.addTest(TestAdd("test_bb"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
