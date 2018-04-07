#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# driver = webdriver.Remote(
    # command_executor='http://127.0.0.1:4444/wd/hub',
    # desired_capabilities=DesiredCapabilities.CHROME)  
    
# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("Selenium2")
# driver.find_element_by_id("su").click()
# driver.quit()


# localhost windows(192.168.2.41):
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>java -jar selenium-server-standalone-3.11.0.jar -role hub

# remote ubuntu 16(192.168.157.130):
# han@han-virtual-machine:~$ java -jar selenium-server-standalone-3.11.0.jar -role node -port 5555 -hub http://192.168.2.41:4444/grid/register

lists = {"http://192.168.157.130:5555/wd/hub": 'firefox'}

for host, browser in lists.items():
    print(host, browser)
    driver = webdriver.Remote(
        command_executor=host,
        desired_capabilities={"browserName": browser,
                              "version": "",
                              "platform": "ANY",})
    # C:\Users\Han\Anaconda3\Lib\site-packages\selenium\webdriver\common\desired_capabilities.py

    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("Selenium2")
    driver.find_element_by_id("su").click()
    # driver.quit()

    