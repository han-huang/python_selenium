#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

#向cookie 的name 和value 添加會話信息。
driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbbbb'})
#遍歷cookies 中的name 和value 資訊列印，當然還有上面添加的資訊
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

# driver.quit()


