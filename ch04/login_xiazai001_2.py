#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import getpass
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.xiazai001.com/forum.php")

title = driver.title
print(title)

now_url = driver.current_url
print(now_url)

sleep(1)
# http://selenium-python.readthedocs.io/locating-elements.html
# http://selenium-python.readthedocs.io/api.html

driver.find_element_by_id("ls_username").clear()
# username = input("Enter your username:")
username = getpass.getpass("Enter your username:")
driver.find_element_by_id("ls_username").send_keys(username)

driver.find_element_by_id("ls_password").clear()
# pw = input("Enter your password:")
pw = getpass.getpass("Enter your password:")
driver.find_element_by_id("ls_password").send_keys(pw)

driver.find_element_by_xpath('//button[@type="submit" and @tabindex="904"]').click()

sleep(1)

user = driver.find_element_by_xpath('//strong[@class="vwmy"]')
print(user.text)

# driver.quit()

