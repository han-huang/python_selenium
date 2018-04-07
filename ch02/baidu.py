# -*- coding: utf-8 -*-
from selenium import webdriver

# browser = webdriver.Firefox()
# browser.get('http://seleniumhq.org/')

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
driver.quit()
