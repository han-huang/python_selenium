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
    unittest.main()


# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch07>python caltest_unittest_test_sequence.py
# test TestAdd start
# test TestAdd test_bb
# test TestAdd end
# .test TestB start
# test TestB test_1
# test TestB end
# .test TestB start
# test TestB test_aa
# test TestB end
# .test TestB start
# test TestB test_cc
# test TestB end
# .
# ----------------------------------------------------------------------
# Ran 4 tests in 0.005s

# OK





# Order of tests in python unittest

# https://stackoverflow.com/questions/30286268/order-of-tests-in-python-unittest

# Option 1.

# One solution to this (as a workaround) was given here - which suggests writing the tests in numbered methods step1, step2, etc., then collecting and storing them via dir(self) and yielding them to one test_ method which trys each.

# Not ideal but does what you expect. Each test sequence has to be a single TestClass (or adapt the method given there to have more than one sequence generating method).

# Option 2.

# Another solution, also in the linked question, is you name your tests alphabetically+numerically sorted so that they will execute in that order.

# But in both cases, write monolithic tests, each in their own Test Class.

# P.S. I agree with all the comments that say unit testing shouldn't be done this way; but there are situations where unit test frameworks (like unittest and pytest) get used to do integration tests which need modular independent steps to be useful. Also, if QA can't influence Dev to write modular code, these kinds of things have to be done.


# https://stackoverflow.com/a/5387956/1431750