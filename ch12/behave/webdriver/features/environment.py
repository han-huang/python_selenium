#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver

# https://testingbot.com/support/getting-started/python.html
# http://behave.readthedocs.io/en/stable/tutorial.html#environmental-controls

# 注意C:\Users\Han\selenium_test\ch12\behave\webdriver\features\environment.py 的路徑 是在features目錄下

def before_all(context):
    # desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    # desired_capabilities['version'] = 'latest'
    # desired_capabilities['platform'] = 'WINDOWS'
    # desired_capabilities['name'] = 'Testing Selenium with Behave'
    # desired_capabilities['client_key'] = 'key'
    # desired_capabilities['client_secret'] = 'secret'

    # context.browser = webdriver.Remote(
        # desired_capabilities=desired_capabilities,
        # command_executor="https://hub.testingbot.com/wd/hub"
    # )

    context.browser = webdriver.Firefox()

def after_all(context):
    context.browser.quit()
