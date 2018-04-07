#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
import threading
from selenium import webdriver
from selenium.webdriver import ChromeOptions



def test_baidu(browser, search):
    print('start %s' % ctime())
    print('browser %s' % browser)
    err_msg = "browser參數有誤: 只能為edge, chrome, ff"

    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)

    if browser == "edge":
        driver = webdriver.Edge()
    elif browser == "chrome":
        # https://stackoverflow.com/questions/43612340/chromedriver-closing-after-test
        # If you want chrome and chromedriver to stay open afterward, you can add the detach option when starting chromedriver
        driver = webdriver.Chrome(chrome_options=opts)
    elif browser == "ff":
        driver = webdriver.Firefox()
    else:
        print(err_msg)

	# can not use the dictionary get(key[, default]) method here
    # driver = None
    # dict_driver = {"edge": "webdriver.Edge()", 
                   # "chrome": "webdriver.Chrome(chrome_options=opts)",
                   # "ff": "webdriver.Firefox()"}
    # driver_str = dict_driver.get(browser, None)
    # assert driver_str, err_msg
    # exec(driver_str, driver) # AttributeError: 'NoneType' object has no attribute 'get'

    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(search)
    driver.find_element_by_id("su").click()
    # sleep(10)
    # driver.quit()

# class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
# args=() -> tuple -> need ","
# https://docs.python.org/3/library/threading.html#threading.Thread
# http://www.runoob.com/python3/python3-multithreading.html
def run_threads():
    # lists = {"chrome": "threading", "ff": "selenium", "edge": "python"}
    lists = {"ie": "threading"}
    threads = []
    # targets = range(len(lists))
    for browser, search in lists.items():
        t = threading.Thread(target=test_baidu, args=(browser, search))
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    run_threads()
    print('%-20s  %s' % ('at the end', ctime()))
