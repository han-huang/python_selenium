#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('textarea.html')
print(file_path)
driver.get(file_path)
text = "selenium test"
js = "var area = document.getElementById('area'); area.value='" + text + "';"
driver.execute_script(js)
# driver.quit()
