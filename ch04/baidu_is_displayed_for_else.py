#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
print(ctime())

for i in range(10) :
    try:
        ele = driver.find_element_by_id("kw22") # 故意用kw22這個錯誤的id 引發印出time out
        if ele.is_displayed():
            break
    except:
        pass

    sleep(1)
else:
    print("time out")

driver.close
print(ctime())
# driver.quit()