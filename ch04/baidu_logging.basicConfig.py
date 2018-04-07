#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import logging
# http://zwindr.blogspot.tw/2016/08/python-logging.html
# https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

# https://docs.python.org/3/library/logging.html#logging.basicConfig
logging.basicConfig(level=logging.DEBUG)
diver = webdriver.Firefox()
diver.get("http://www.baidu.com")
diver.find_element_by_id("kw").send_keys("selenium")
diver.find_element_by_id("su").click()
diver.quit()

# https://docs.python.org/3/library/logging.html#logging-levels
# Level	Numeric value
# CRITICAL	50
# ERROR	40
# WARNING	30
# INFO	20
# DEBUG	10
# NOTSET	0
