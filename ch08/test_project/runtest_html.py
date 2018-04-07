#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from HtmlTestRunner import HTMLTestRunner

if __name__ == '__main__':
    test_dir = './test_project/test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(output='example_suite')
    runner.run(discover)

    # https://github.com/oldani/HtmlTestRunner
    
    # Just import HtmlTestRunner from package, then pass it to unittest.main with the testRunner keyword. This class have only one required parameter, with is output this is use to place the report of the TestCase, this is saved under a reports directory.
    
    # C:\Users\Han\selenium_test\ch08\reports\example_suite
    
    # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch08>python test_project\runtest_html.py
    
    # Running tests...
    # ----------------------------------------------------------------------
    # test_baidu (test_baidu.MyTest) ... OK (16.074188)s
    # test_youdao (test_youdao.MyTest) ... OK (26.967984)s
    
    # ----------------------------------------------------------------------
    # Ran 2 tests in 0:00:43
    
    # OK



    # Generating HTML reports...


    # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch08>dir reports\example_suite \s
