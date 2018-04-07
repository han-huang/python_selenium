#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

first_url = "https://www.google.com.tw"
print("now access %s" % first_url)
driver.get(first_url)
sleep(1)

second_url = "https://news.google.com/news/?ned=tw&hl=zh-TW&gl=TW"
print("now access %s" % second_url)
driver.get(second_url)
sleep(1)

print("back to %s" % first_url)
driver.back()
sleep(1)

print("forward to %s" % second_url)
driver.forward()
sleep(1)

stock_url = "https://tw.stock.yahoo.com/"
print("now access %s" % stock_url)
driver.get(stock_url)
sleep(2)

for i in range(1, 11):
    print("%d refresh" %i)
    driver.refresh()
    sleep(2)

# driver.quit()
