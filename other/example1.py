# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# https://pypi.python.org/pypi/selenium
# Example 0:
# open a new Firefox browser
# load the Yahoo homepage
# search for “seleniumhq”
# close the browser

browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()
