#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
print(ctime())

size=driver.find_element_by_id('kw').size
print(size)
#返回百度頁面底部備案資訊
text=driver.find_element_by_id("cp").text
print(text)
#返回元素的屬性值，可以是id、name、type 或元素擁有的其它任意屬性
attribute=driver.find_element_by_id("kw").get_attribute('type')
print(attribute)
#返回元素的結果是否可見，返回結果為True 或False
result=driver.find_element_by_id("kw").is_displayed()
print(result)
driver.quit()
