#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
from selenium import webdriver

def browser():
    host = '127.0.0.1:4444'
    dc = {"browserName": 'chrome'}
    driver = webdriver.Remote(command_executor='http://' + host + '/wd/hub',
                              desired_capabilities=dc)
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()

