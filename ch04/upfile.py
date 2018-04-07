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

#打開上傳功能頁面
file_path = 'file:///' + os.path.abspath('upfile.html')
print(file_path)
driver.get(file_path)
upload = os.path.abspath(os.path.splitext(__file__)[0] + ".txt")
print(upload)

output_source()

#定位上傳按鈕，添加本地檔
driver.find_element_by_name("file").send_keys(upload)

# driver.quit()
