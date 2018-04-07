#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def output_source():
    with open(os.path.splitext(__file__)[0] + ".txt", mode='w', encoding='utf-8') as out_file:
        out_file.write(driver.page_source)

driver = webdriver.Firefox()
# driver = webdriver.Chrome()

#打開上傳功能頁面
file_path = 'file:///' + os.path.abspath('upfile.html')
print(file_path)
driver.get(file_path)
# upload = os.path.abspath(os.path.splitext(__file__)[0] + ".txt")
# print(upload)

output_source()

#定位上傳按鈕，添加本地檔
# driver.find_element_by_name("file").send_keys(upload)

# driver.find_element_by_name("file").click()
ele = driver.find_element_by_name("file")
print(ele.get_attribute("outerHTML"))
# ele.click()

# use webdriver.Firefox() driver.find_element_by_name("file").click() -> selenium.common.exceptions.InvalidArgumentException: Message: Cannot click <input type=file> elements
# https://stackoverflow.com/questions/9726005/how-to-click-on-input-type-file-across-browsers-using-selenium-webdriver
# use driver.execute_script instead of driver.find_element_by_name("file").click()
driver.execute_script('arguments[0].click();', ele)


#調用upfile.exe 上傳程式
# use \\ for SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 28-29: truncated \uXXXX escape
os.system("C:\\Users\\Han\\selenium_test\\ch04\\upfile.exe") # upfile.exe (compile upfile.au3)
# os.system("C:\\Users\\Han\\AutoIt_example\\upfile_chrome.exe")

# driver.quit()
