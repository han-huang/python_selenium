# -*- coding: utf-8 -*-
from selenium import webdriver

# http://selenium-python.readthedocs.io/locating-elements.html
# http://selenium-python.readthedocs.io/api.html

driver = webdriver.Firefox()
driver.get("https://news.google.com/news/headlines?ned=tw&hl=zh-TW&gl=TW")
size = driver.find_element_by_xpath('//input[@class="Ax4B8 ZAGvjd" and @aria-label="搜尋"]').size
print(size)

text = driver.find_element_by_xpath('//span[@jsname="QiyZ6c" and @class="adH5zf"]').text
print(text)

# http://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webelement.WebElement.get_attribute
attr = driver.find_element_by_xpath('//span[@jsname="QiyZ6c" and @class="adH5zf"]').get_attribute("jsname")
print(attr)

ret = driver.find_element_by_xpath('//span[@jsname="QiyZ6c" and @class="adH5zf"]').is_displayed()
print(ret)

# ret = driver.find_element_by_xpath('//input[@jsname="A51lKb"]').is_displayed()
# print(ret)
# driver.quit()
