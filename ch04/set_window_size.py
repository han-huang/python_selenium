#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://mail.google.com")

# 參數字為像素點
print("設定瀏覽器寬480 高800顯示")
driver.set_window_size(480, 800)
# driver.quit()

