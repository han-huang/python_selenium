#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime, sleep

driver = webdriver.Firefox()
# http://selenium-python-zh.readthedocs.io/en/latest/waits.html
# http://selenium-python.readthedocs.io/waits.html#implicit-waits
driver.implicitly_wait(10) # seconds
driver.get("http://www.baidu.com")

try:
    print(ctime())
    ele = driver.find_element_by_id("kw22").send_keys("selenium") # 故意用kw22這個錯誤的id 引發exception
    # ele = driver.find_element_by_id("kw").send_keys("selenium") # kw正確的id
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
# driver.quit()
