#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
from selenium import webdriver
# from driver import browser
import unittest, os, sys
# print(os.path.join(os.path.dirname(__file__), os.path.pardir))
print(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
from models.driver import browser

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_baidu(self):
        print(sys._getframe().f_code.co_name) # https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string-in-python
        driver = self.driver
        driver.get('http://www.baidu.com')
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        sleep(2)
        title = driver.title
        self.assertEqual(title, "unittest_百度搜索")

    def tearDown(self):
        # self.driver.quit()
        pass

if __name__ == '__main__':
    unittest.main()



# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>python ch09\run_selenium-server.py

# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch11>python test_case\models\myunit.py
# test_baidu
# .
# ----------------------------------------------------------------------
# Ran 1 test in 8.149s

# OK

    