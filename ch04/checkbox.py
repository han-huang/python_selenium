#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
import os
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('checkbox.html')
print(file_path)
driver.get(file_path)
# 选择页面上所有的tag name 为input 的元素
inputs = driver.find_elements_by_tag_name('input')
#然后从中过滤出tpye 为checkbox 的元素，单击勾选
for i in inputs:
    # http://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webelement.WebElement.get_attribute
    if i.get_attribute('type') == 'checkbox':
        i.click()
        sleep(1)

driver.quit()


# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch04>python checkbox.py
# file:///C:\Users\Han\selenium_test\ch04\checkbox.html
