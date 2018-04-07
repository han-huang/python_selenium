#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
import os

def output_source():
    with open(os.path.splitext(__file__)[0] + ".txt", mode='w', encoding='utf-8') as out_file:
        out_file.write(driver.page_source)

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('frame.html')
print(file_path)

# http://selenium-python-zh.readthedocs.io/en/latest/waits.html
# http://selenium-python.readthedocs.io/waits.html#implicit-waits
driver.implicitly_wait(10) # seconds

driver.get(file_path)

#切換到iframe（id = "if"）
# driver.switch_to.frame("if")


#先通過xpth 定位到iframe
xf = driver.find_element_by_xpath('//*[@id="if"]')
#再將定位對象傳給switch_to.frame()方法
driver.switch_to.frame(xf)


# output_source()

#下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
# sleep(3)


# http://blog.csdn.net/huilan_same/article/details/52200586
# http://selenium-python.readthedocs.io/api.html?highlight=default_content#selenium.webdriver.remote.webdriver.WebDriver.switch_to
# driver.switch_to.default_content()
driver.switch_to.parent_frame()

output_source()

driver.close
# driver.quit()


