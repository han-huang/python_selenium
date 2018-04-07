# -*- coding: utf-8 -*-
from selenium import webdriver

# https://pypi.python.org/pypi/selenium
# Example 0:
# open a new Firefox browser
# load the page at the given URL

browser = webdriver.Firefox()
browser.get('http://seleniumhq.org/')

# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("Selenium2")
# driver.find_element_by_id("su").click()
# driver.quit()
