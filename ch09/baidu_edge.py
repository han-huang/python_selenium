#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Edge()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
sleep(1)
driver.quit()

