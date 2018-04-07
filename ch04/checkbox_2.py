#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
import os
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('checkbox.html')
print(file_path)
driver.get(file_path)
		
#通過XPath 找到type=checkbox 的元素
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
#通過CSS 找到type=checkbox 的元素
# checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')

for checkbox in checkboxes:
    checkbox.click()
    sleep(1)
# 列印當前頁面上type 為checkbox 的個數
print(len(checkboxes))
# 把頁面上最後1 個checkbox 的勾給去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
sleep(1)
# remove first one
driver.find_elements_by_css_selector('input[type=checkbox]').pop(0).click()

# driver.quit()


# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch04>python checkbox_2.py
# file:///C:\Users\Han\selenium_test\ch04\checkbox.html
# 3
