# Please visit http://selenium-python.readthedocs.org/en/latest/index.html for detailed installation and instructions
# Getting started: http://docs.seleniumhq.org/
# API details: https://github.com/SeleniumHQ/selenium#selenium

# Requests is the easiest way to make RESTful API calls in Python. You can install it by following the instructions here:
# http://docs.python-requests.org/en/master/user/install/

# refer to https://github.com/crossbrowsertesting/selenium-python/blob/master/drag-and-drop.py

import unittest
from selenium import webdriver
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()
driver = webdriver.Firefox()

# load the page url
print('Loading Url')
# driver.get('http://crossbrowsertesting.github.io/drag-and-drop.html')
# driver.get('https://www.w3schools.com/html/html5_draganddrop.asp') # not working, ???
driver.get('https://dev.opera.com/articles/accessible-drag-and-drop/example.html')

# maximize the window - DESKTOPS ONLY
print('Maximizing window')
driver.maximize_window()

# grab the first element
print('Grabbing draggable element')
draggable = driver.find_element_by_xpath("//li[contains(text(), 'Babyshambles')]")

# then the second element
print('Grabbing the droppable element')
droppable = driver.find_element_by_id("Tol")

# we use ActionChains to move the element
print('Dragging the element')
actionChains = ActionChains(driver)
actionChains.drag_and_drop(draggable, droppable).perform()


