#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Firefox()
# file_path = 'file:///' + os.path.abspath('textarea.html')
# print(file_path)
driver.get("http://videojs.com/")
video = driver.find_element_by_id("preview-player_html5_api")
url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)
print("start")
driver.execute_script("return arguments[0].play()", video)
sleep(5)
driver.execute_script("arguments[0].pause()", video)

# driver.quit()
