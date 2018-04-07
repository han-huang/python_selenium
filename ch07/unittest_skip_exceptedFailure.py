#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

# https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures

class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    @unittest.skip("直接跳過測試")
    def test_skip(self):
        print("test skip")

    @unittest.skipIf(3 > 2, "當條件為True時跳過測試")
    def test_skip_if(self):
        print("test skip if")       

    @unittest.skipUnless(3 > 2, "當條件為True時執行測試")
    def test_skip_unless(self):
        print("test skipUnless")        

    @unittest.expectedFailure
    def test_excepted_failure(self):
        assertEqual(2, 3)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
