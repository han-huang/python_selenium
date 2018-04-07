#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

if __name__ == '__main__':
    test_dir = './test_project/test_case'
    # use the following command according to your position
    # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch07>python test_project\runtest.py
    # test_baidu
    # .test_youdao
    # .
    # ----------------------------------------------------------------------
    # Ran 2 tests in 23.785s
    
    # OK

    # Anaconda3: output to test_project\report\log.txt
    # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch07>python test_project\runtest.py > test_project\report\log.txt 2>&1

    # ms-dos: output to test_project\report\log.txt
    # C:\Users\Han\selenium_test\ch07>C:\Users\Han\Anaconda3\python.exe test_project\runtest.py > test_project\report\log.txt 2>&1
    
    
    # test_dir = './test_case'
    # use the following command
    # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch07\test_project>python runtest.py
    # test_baidu
    # .test_youdao
    # .
    # ----------------------------------------------------------------------
    # Ran 2 tests in 28.556s
    
    # OK

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)
