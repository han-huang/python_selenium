#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from calculator import Count
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        number = input("Enter a number:")
        self.number = int(number)
        
    def test_case(self):
        self.assertEqual(self.number, 10, msg="You input is not 10!")

    def tearDown(self):
        print('test end')

if __name__ == '__main__':
    unittest.main()

# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual

# assertEqual(first, second, msg=None)

# Test that first and second are equal. If the values do not compare equal, the test will fail.

# In addition, if first and second are the exact same type and one of list, tuple, dict, set, frozenset or str or any type that a subclass registers with addTypeEqualityFunc() the type-specific equality function will be called in order to generate a more useful default error message (see also the list of type-specific methods).

# Changed in version 3.1: Added the automatic calling of type-specific equality function.

# Changed in version 3.2: assertMultiLineEqual() added as the default type equality function for comparing strings.
