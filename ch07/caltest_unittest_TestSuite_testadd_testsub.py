#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from calculator import Count
import unittest

class TestAdd(unittest.TestCase):

    def setUp(self):
        print('test add start')
        
    def test_add(self):
        j = Count(2, 3)
        # j = Count(2, 6)
        self.assertEqual(j.add(), 5)

    def test_add_2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)      
    
    def tearDown(self):
        print('test add end')

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
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))
    suite.addTest(TestAdd("test_add_2"))
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub_2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

# addTest(test)
# https://docs.python.org/3/library/unittest.html#unittest.TestSuite.addTest


# https://docs.python.org/3/library/unittest.html#organizing-test-code

# If setUp() succeeded, tearDown() will be run whether the test method succeeded or not.

# Such a working environment for the testing code is called a fixture.

# Test case instances are grouped together according to the features they test. unittest provides a mechanism for this: the test suite, represented by unittest’s TestSuite class. In most cases, calling unittest.main() will do the right thing and collect all the module’s test cases for you, and then execute them.

# However, should you want to customize the building of your test suite, you can do it yourself:

# def suite():
    # suite = unittest.TestSuite()
    # suite.addTest(WidgetTestCase('test_default_widget_size'))
    # suite.addTest(WidgetTestCase('test_widget_resize'))
    # return suite

# if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suite())