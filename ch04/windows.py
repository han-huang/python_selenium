#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def output_source():
    with open(os.path.splitext(__file__)[0] + ".txt", mode='w', encoding='utf-8') as out_file:
        out_file.write(driver.page_source)

driver = webdriver.Firefox()


# http://selenium-python-zh.readthedocs.io/en/latest/waits.html
# http://selenium-python.readthedocs.io/waits.html#implicit-waits
driver.implicitly_wait(10) # seconds

driver.get("http://www.baidu.com")
#獲得百度搜索窗口控制碼
sreach_windows= driver.current_window_handle
all_handles = driver.window_handles
print(all_handles)

# driver.get("https://passport.baidu.com/v2/?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2F&amp;sms=5")
# driver.find_element_by_link_text('登录').click()

# ele = WebDriverWait(driver, 5, 0.5).until(
    # EC.presence_of_element_located((By.LINK_TEXT,"登录"))
# )

# ele = driver.find_element_by_link_text('登录')

# not only one tj_login, use find_elements_by_xpath or find_elements_by_link_text
# eles = driver.find_elements_by_xpath('//a[@name="tj_login"]')
eles = driver.find_elements_by_link_text('登录')
for ele in eles:
    print(ele.text)
    print(ele.get_attribute('href'))
eles[1].click() # click the second element

all_handles = driver.window_handles
print(all_handles)
# http://selenium-python-zh.readthedocs.io/en/latest/waits.html
# http://selenium-python.readthedocs.io/waits.html#explicit-waits
element = WebDriverWait(driver, 5, 0.5).until(
    EC.presence_of_element_located((By.LINK_TEXT,"立即注册"))
)
print(element.text)
print(element.get_attribute('href'))

# for debug
# elements = driver.find_elements_by_link_text('立即注册')
# for element in elements:
    # print(element.text)
    # print(element.get_attribute('href'))

element.click()

driver.implicitly_wait(10) # seconds

#獲得當前所有打開的視窗的控制碼
all_handles = driver.window_handles
#進入註冊視窗
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        print(handle)
        print(all_handles)

        element = WebDriverWait(driver, 5, 0.5).until(
            EC.presence_of_element_located((By.ID,"TANGRAM__PSP_3__userName"))
        )
        print(element.get_attribute('name'))
        element.send_keys('goodjob')
        # element = driver.find_element_by_id("TANGRAM__PSP_3__userName")
        # print(element.get_attribute('name'))
        # element.send_keys('goodjob')

        # elements = driver.find_elements_by_id("TANGRAM__PSP_3__userName")
        # for element in elements:
            # print(element.get_attribute('name'))

        element = WebDriverWait(driver, 5, 0.5).until(
            EC.presence_of_element_located((By.ID,"TANGRAM__PSP_3__password"))
        )
        print(element.get_attribute('name'))
        element.send_keys('p1a2s3s4word')
        # element = driver.find_element_by_id('TANGRAM__PSP_3__password')
        # print(element.get_attribute('name'))
        # element.send_keys('p1a2s3s4word')

        # elements = driver.find_elements_by_id('TANGRAM__PSP_3__password')
        # for element in elements:
            # print(element.get_attribute('name'))
        sleep(1)

#進入搜索視窗
for handle in all_handles:
    if handle == sreach_windows:
        driver.switch_to.window(handle)
        print('now sreach window!')
        print(handle)
        driver.find_element_by_id('TANGRAM__PSP_4__closeBtn').click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        sleep(1)

driver.close
# driver.quit()


