#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Opera\\launcher.exe"
driver = webdriver.Opera(options=options)
# driver = webdriver.Opera()

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
# driver.quit()
driver.close()

# https://github.com/operasoftware/operachromiumdriver/issues/31
# It works with mentioned by ghost hotfix:

# from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.binary_location = "/usr/bin/opera" # getting error without this line
# browser = webdriver.Opera(options=options)
# browser.get('http://seleniumhq.org/')
# browser.quit()
