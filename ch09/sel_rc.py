#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import selenium

sel = selenium("localhost", 4444, "*firefox", "http://www.baidu.com/")
sel.start()

sel.open("/")
sel.type("id=kw", "selenium grid")
sel.click("id=su")
sel.wait_for_page_to_load("30000")

sel.stop()



# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch09>python sel_rc.py
# Traceback (most recent call last):
  # File "sel_rc.py", line 3, in <module>
    # from selenium import selenium
# ImportError: cannot import name 'selenium'


# https://www.seleniumhq.org/download/

# Selenium 3.X is no longer capable of running Selenium RC directly, rather it does it through emulation and the WebDriverBackedSelenium interface.

# Download version 3.11.0





# https://stackoverflow.com/questions/45577940/selenium-module-calling-error

# Update

# You are using Selenium's version 3.+

# As it reads here https://seleniumhq.wordpress.com/2016/10/13/selenium-3-0-out-now/

# The major change in Selenium 3.0 is we’re removing the original Selenium Core implementation and replacing it with one backed by WebDriver. This will affect all users of the Selenium RC APIs.

# This is very likely the reason why your code is not working anymore. You have two solutions. Either you downgrade your version of selenium (which is rarely a good idea), or you must re-develop a new testing framework which works with this new version.







