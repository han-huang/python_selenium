#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
#引入Keys 模組
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(3)
#輸入框輸入內容
driver.find_element_by_id("kw").send_keys("seleniumm")
sleep(1)
#刪除多輸入的一個m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
sleep(1)
#輸入空白鍵+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
sleep(1)
driver.find_element_by_id("kw").send_keys(" 教程")
sleep(1)
#ctrl+a 全選輸入框內容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
sleep(1)
#ctrl+x 剪切輸入框內容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
sleep(1)
#ctrl+v 粘貼內容到輸入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
sleep(1)
#通過enter來代替點擊操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
# driver.quit()
