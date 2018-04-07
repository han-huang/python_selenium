#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep

driver = webdriver.Firefox()
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
target = driver.find_element_by_xpath('//span[@class="context-menu-one btn btn-neutral"]')

# http://jashliao.pixnet.net/blog/post/220872427-python-%E7%A8%8B%E5%BC%8F%E9%81%8E%E9%95%B7%E6%99%82%E7%9A%84%E6%8F%9B%E8%A1%8C%E8%AA%9E%E6%B3%95%5B%5C%5D
# ActionChains(driver).context_click(target).key_down(Keys.ARROW_DOWN)\
# .key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).send_keys(Keys.ENTER).send_keys(Keys.ENTER).perform()

current_window = driver.current_window_handle
print(current_window)


# http://selenium-python.readthedocs.io/api.html?highlight=get_attribute#module-selenium.webdriver.common.action_chains
actions = ActionChains(driver)
actions.context_click(target) # right click
actions.key_down(Keys.ARROW_DOWN)
actions.key_down(Keys.ARROW_DOWN)
actions.key_down(Keys.ARROW_DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()


sleep(1)


all_window = driver.window_handles
print(all_window)

# http://selenium-python.readthedocs.io/api.html?highlight=get_attribute#module-selenium.webdriver.common.alert
# print(Alert(driver).text)
# Alert(driver).accept()


# https://stackoverflow.com/questions/8631500/click-the-javascript-popup-through-webdriver
# http://selenium-python.readthedocs.io/api.html?highlight=get_attribute#selenium.webdriver.remote.webdriver.WebDriver.switch_to_alert
# http://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.switch_to
# use switch_to.alert
try:
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
except:
    print("no alert to accept")


# current_window = driver.current_window_handle
# driver.switch_to.window(current_window)


# driver.quit()
