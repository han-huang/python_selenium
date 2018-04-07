#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep
import os
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup
from pprint import pprint

def output_source():
    with open(os.path.splitext(__file__)[0] + ".txt", mode='w', encoding='utf-8') as out_file:
        out_file.write(driver.page_source)

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.set_window_size(1500, 1000)

# driver.get("https://www.w3schools.com/html/html5_draganddrop.asp") # not working, ???
driver.get('https://dev.opera.com/articles/accessible-drag-and-drop/example.html')

actions = ActionChains(driver)
# ele = driver.find_element_by_id("div1")
ele = driver.find_element_by_xpath("//li[contains(text(), 'Babyshambles')]")

attrs = ele.get_property('attributes')
print(type(attrs))
# print(attrs['0'])
html = ele.get_attribute('outerHTML')
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
soup = BeautifulSoup(html, 'html.parser')

# pprint(drag1.get("src"))
# div1 = soup.find(id="div1")
# pprint(div1.get("ondrop"))
# pprint(div1)


# https://stackoverflow.com/questions/31958637/beautifulsoup-search-by-text-inside-a-tag
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#the-string-argument

Babyshambles = soup.find("li", string="Babyshambles")
pprint(Babyshambles.get("class"))
pprint(Babyshambles.text)
pprint(Babyshambles)

# print(ele)

# target = driver.find_element_by_id("div2")
target = driver.find_element_by_id("Tol")
html_target = target.get_attribute('outerHTML')
soup_target = BeautifulSoup(html_target, 'html.parser')
Tol = soup_target.find(id="Tol")
pprint(Tol)
actions.drag_and_drop(ele, target).perform()

# output_source()

# driver.quit()
