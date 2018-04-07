#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from HtmlTestRunner import HTMLTestRunner

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
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(output='example_suite')
    runner.run(discover)

    # https://github.com/oldani/HtmlTestRunner
    
    # Just import HtmlTestRunner from package, then pass it to unittest.main with the testRunner keyword. This class have only one required parameter, with is output this is use to place the report of the TestCase, this is saved under a reports directory.
    
    # C:\Users\Han\selenium_test\ch07\reports\example_suite
    
    # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch07>python test_project\runtest_html.py
    
    # Running tests...
    # ----------------------------------------------------------------------
    # test_baidu (test_baidu.MyTest) ... OK (9.728881)s
    # test_youdao (test_youdao.MyTest) ... OK (11.525394)s
    
    # ----------------------------------------------------------------------
    # Ran 2 tests in 0:00:21
    
    # OK
    
    
    
    # Generating HTML reports...
    
    # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch07>dir reports\example_suite \s
    # 磁碟區 C 中的磁碟沒有標籤。
    # 磁碟區序號:  3E9E-61A9
    
    # C:\Users\Han\selenium_test\ch07\reports\example_suite 的目錄
    
    # 2018/03/26  上午 12:56    <DIR>          .
    # 2018/03/26  上午 12:56    <DIR>          ..
    # 2018/03/26  上午 12:56             2,989 Test_test_baidu.MyTest_2018-03-26_00-56-34.html
    # 2018/03/26  上午 12:56             2,991 Test_test_youdao.MyTest_2018-03-26_00-56-34.html
                # 2 個檔案           5,980 位元組
