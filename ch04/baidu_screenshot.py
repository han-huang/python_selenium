#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
from selenium import webdriver
import os
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# http://selenium-python.readthedocs.io/api.html?highlight=get_screenshot_as_file#selenium.webdriver.remote.webdriver.WebDriver.get_screenshot_as_file
# get_screenshot_as_file(filename)
#     Saves a screenshot of the current window to a PNG image file. Returns
#         False if there is any IOError, else returns True. Use full paths in your filename.
#     Args:	
#     filename: The full path you wish to save your screenshot to. This should end with a .png extension.
#     Usage:
#     driver.get_screenshot_as_file(‘/Screenshots/foo.png’)
save = os.getcwd() + '\\' + os.path.splitext(__file__)[0] + ".png"
try:
    driver.find_element_by_id('kw_error').send_key('selenium')
    driver.find_element_by_id('su').click()
except:
    driver.get_screenshot_as_file(save)
    # driver.quit()
