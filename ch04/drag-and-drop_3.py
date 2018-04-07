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
from time import sleep

# driver = webdriver.Chrome()
driver = webdriver.Firefox()
# driver = webdriver.Edge()

# load the page url
print('Loading Url')
# driver.get('http://crossbrowsertesting.github.io/drag-and-drop.html')
driver.get('https://www.w3schools.com/html/html5_draganddrop.asp') # not working, ???
# driver.get('https://html5demos.com/drag/') # not working, ???
# driver.get('https://dev.opera.com/articles/accessible-drag-and-drop/example.html')

# maximize the window - DESKTOPS ONLY
print('Maximizing window')
driver.maximize_window()

# actionChains.drag_and_drop(draggable, droppable).perform() not working, use script
drag_and_drop_script = 'drag1 = document.getElementById("drag1");document.getElementById("div2").appendChild(drag1);'
print('use script to drag and drop')
driver.execute_script(drag_and_drop_script)

# grab the first element
# print('Grabbing draggable element')
# draggable = driver.find_element_by_xpath('//img[@src="img_w3slogo.gif"]')

# draggable = driver.find_element_by_xpath('//img[@ondragstart="drag(event)"]')
# draggables = driver.find_elements_by_xpath('//img[@ondragstart="drag(event)"]')
# print('len(draggables)', len(draggables))
# img_src = draggable.get_attribute('src') # img_src https://www.w3schools.com/html/img_w3slogo.gif
# print("img_src", img_src)




# then the second element
# print('Grabbing the droppable element')
# droppable = driver.find_element_by_id("div2")
# droppables = driver.find_elements_by_id("div2")
# print('len(droppables)', len(droppables))
# ondrop = droppable.get_attribute('ondrop')
# print("ondrop", ondrop)
# we use ActionChains to move the element
# print('Dragging the element')
# actionChains = ActionChains(driver)
# actionChains.click_and_hold(draggable).move_to_element(droppable).release().perform()

# actionChains.click_and_hold(draggable)
# actionChains.move_to_element(droppable)
# actionChains.release()
# actionChains.perform()

# actionChains.drag_and_drop(draggable, droppable).perform()
# actionChains.drag_and_drop_by_offset(draggable, 0, 120).perform()
# actionChains.context_click(draggable).perform()
# sleep(1)
# actionChains.drag_and_drop(draggable, droppable).perform()
# sleep(1)


# https://html5demos.com/drag/ # not working, ???
# draggable=driver.find_element_by_id("two")
# droppable=driver.find_element_by_id("bin")

# actionChains = ActionChains(driver)
# actionChains.drag_and_drop(draggable, droppable).perform()
# actionChains.drag_and_drop(droppable, draggable).perform()
