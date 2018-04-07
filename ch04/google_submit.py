# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.google.com.tw")
driver.find_element_by_id("lst-ib").send_keys("Selenium")
driver.find_element_by_id("lst-ib").submit()
# driver.quit()
