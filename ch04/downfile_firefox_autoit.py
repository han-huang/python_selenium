#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml,application/octet-stream,application/gzip"

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
# http://kb.mozillazine.org/Firefox_:_FAQs_:_About:config_Entries
fp.set_preference("browser.download.dir", os.getcwd())
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream") #下載檔案的類型
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
fp.set_preference("browser.helperApps.neverAsk.openFile", mime_types)
fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
fp.set_preference("pdfjs.disabled", True);  # disable the built-in PDF viewer
fp.set_preference("browser.download.panel.shown", False)
# fp.set_preference("pdfjs.firstRun", False)  #

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://pypi.Python.org/pypi/selenium")
# driver.find_element_by_partial_link_text("selenium-2").click()
driver.find_element_by_partial_link_text("selenium-3.11.0.tar.gz").click()

# workaround ; use autoit to control keyboard because this can not download automatically 
os.system("C:\\Users\\Han\\selenium_test\\ch04\\downfile_firefox.exe") # downfile_firefox.exe (compile downfile_firefox.au3)


# driver.get("https://www.mozilla.org/en-US/foundation/documents")
# driver.find_element(By.LINK_TEXT, "IRS Form 872-C").click()


# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()

# 這些參數的設置可以通過在Firefox 瀏覽器位址欄輸入：about:config 進行設置