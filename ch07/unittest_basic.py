#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://docs.python.org/3/library/unittest.html
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

            # s.split('2')
            # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch07>python unittest_basic.py
            # .F.
            # ======================================================================
            # FAIL: test_split (__main__.TestStringMethods)
            # ----------------------------------------------------------------------
            # Traceback (most recent call last):
            # File "unittest_basic.py", line 20, in test_split
                # s.split('2')
            # AssertionError: TypeError not raised
            
            # ----------------------------------------------------------------------
            # Ran 3 tests in 0.001s
            
            # FAILED (failures=1)

if __name__ == '__main__':
    unittest.main()
