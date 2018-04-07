#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.set_window_size(600, 600)

driver.find_element_by_id("kw").send_keys("seleniumm")
driver.find_element_by_id("su").click()
sleep(2)

js = "window.scrollTo(100, 450)"
driver.execute_script(js)
sleep(2)
# driver.quit()
