#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

# https://stackoverflow.com/questions/35331854/downloading-a-file-at-a-specified-location-through-python-and-selenium-using-chr
options = webdriver.ChromeOptions()
# https://stackoverflow.com/questions/40654358/how-to-control-the-download-of-files-with-selenium-python-bindings-in-chrome
# prefs = {'download.default_directory' : os.getcwd(), 
    # "download.prompt_for_download": False,
    # "download.directory_upgrade": True,
    # "safebrowsing.enabled": True }
# options.add_experimental_option('prefs', prefs)

# https://stackoverflow.com/questions/35331854/downloading-a-file-at-a-specified-location-through-python-and-selenium-using-chr
# options.add_argument("download.default_directory=C:/Downloads") # work, download automatically
options.add_argument("download.default_directory=" + os.getcwd()) # work, download automatically

driver = webdriver.Chrome(chrome_options=options)
driver.get("http://pypi.Python.org/pypi/selenium")
# driver.find_element_by_partial_link_text("selenium-2").click()
driver.find_element_by_partial_link_text("selenium-3.11.0.tar.gz").click() 

# workaround ; use autoit to control keyboard because this can not download automatically 
# os.system("C:\\Users\\Han\\selenium_test\\ch04\\downfile_chrome.exe") # downfile_chrome.exe (compile downfile_chrome.au3)


# driver.get("https://www.mozilla.org/en-US/foundation/documents")
# driver.find_element(By.LINK_TEXT, "IRS Form 872-C").click()


