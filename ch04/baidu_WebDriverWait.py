#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# http://selenium-python-zh.readthedocs.io/en/latest/waits.html
# http://selenium-python.readthedocs.io/waits.html#explicit-waits
element = WebDriverWait(driver, 5, 0.5).until(
    EC.presence_of_element_located((By.ID,"kw"))
)
element.send_keys('selenium')
# driver.quit()
