#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
from selenium import webdriver
# from driver import browser
import unittest, os, sys, time
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
from models.driver import browser

def insert_img(driver, file_name):
    base_dir =  os.path.dirname(__file__)
    print('%s %s' % (base_dir, type(base_dir))) # test_case\models <class 'str'>

    base_dir = base_dir.replace('\\', '/')
    print('base_dir %s' % base_dir) # base_dir test_case/models

    # base = base_dir.split('/test_case')[0]    
    base = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)
    base = base.replace('\\', '/')
    print('base %s' % base) # base test_case/models/../..
    # file_path = base + '/report/image/' + file_name
    file_path = base + '/reports/image/' + file_name
    print(file_path) # test_case/models/../../reports/image/baidu_20180404162909.png
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = browser()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://www.baidu.com')
    png = 'baidu_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
    insert_img(driver, png)
    driver.quit

    # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>python ch09\run_selenium-server.py

    # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch11>python test_case\models\function.py

