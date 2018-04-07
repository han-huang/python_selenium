#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep

driver = webdriver.Firefox()
driver.set_window_size(1500, 1000)
driver.get("http://www.books.com.tw/")

# close advertisement banner
print("close ad banner")
driver.find_element_by_xpath('//a[@id="close_top_banner"]').click()

# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
# scroll down
print("scroll down")
driver.execute_script("window.scrollTo(0, 600)") 

def mouse_move(actions, target_li):
    for i in range(len(target_li)):
        ele = '//li[@data-tsource="' + target_li[i] + '"]'
        target = driver.find_element_by_xpath(ele)
        sleep(2)
        print("move to %s" % target.text)
        print(target.location)
        actions.move_to_element(target).perform()

actions = ActionChains(driver)
target_li = ['41012', '79150', '41011', '41013', '41010']
mouse_move(actions, target_li)


# http://selenium-python.readthedocs.io/api.html?highlight=get_attribute#module-selenium.webdriver.common.action_chains
# actions = ActionChains(driver)
# above = driver.find_element_by_xpath('//li[@data-tsource="41012"]')
# print("move to %s" % above.text)
# actions.move_to_element(above).perform()

# sleep(2)
# above_2 = driver.find_element_by_xpath('//li[@data-tsource="79150"]')
# print("move to %s" % above_2.text)
# actions.move_to_element(above_2).perform()

# sleep(2)
# above_3 = driver.find_element_by_xpath('//li[@data-tsource="41011"]')
# print("move to %s" % above_3.text)
# actions.move_to_element(above_3).perform()

# sleep(2)
# above_4 = driver.find_element_by_xpath('//li[@data-tsource="41013"]')
# print("move to %s" % above_4.text)
# actions.move_to_element(above_4).perform()

# sleep(2)
# above_5 = driver.find_element_by_xpath('//li[@data-tsource="41010"]')
# print("move to %s" % above_5.text)
# actions.move_to_element(above_5).perform()

# driver.quit()
