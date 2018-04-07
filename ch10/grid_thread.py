#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep, ctime
import threading
from selenium import webdriver
from selenium.webdriver import ChromeOptions

def test_baidu(host, browser):
    print('%-12s %s' % ('start', ctime()))
    print(host, browser)
    driver = webdriver.Remote(command_executor=host,
                              desired_capabilities={"browserName": browser,
                                                    "version": "",
                                                    "platform": "ANY",})

    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(browser)
    driver.find_element_by_id("su").click()
    # sleep(10)
    # driver.quit()

# class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
# args=() -> tuple -> need ","
# https://docs.python.org/3/library/threading.html#threading.Thread
# http://www.runoob.com/python3/python3-multithreading.html
def run_threads():
    # lists = {"chrome": "threading", "ff": "selenium", "edge": "python"}
    lists = {"http://127.0.0.1:5556/wd/hub": 'chrome',
            "http://127.0.0.1:5557/wd/hub": 'firefox',
            "http://192.168.157.130:5555/wd/hub": 'firefox'}
    threads = []
    # targets = range(len(lists))
    for host, browser in lists.items():
        t = threading.Thread(target=test_baidu, args=(host, browser))
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    run_threads()
    print('%-12s %s' % ('at the end', ctime()))

# localhost windows(192.168.2.41) VMware Network Adapter VMnet1(192.168.91.1):
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>java -jar selenium-server-standalone-3.11.0.jar -role hub
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>java -jar selenium-server-standalone-3.11.0.jar -role node -port 5556
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>java -jar selenium-server-standalone-3.11.0.jar -role node -port 5557

# remote ubuntu 16(192.168.157.130):
# han@han-virtual-machine:~$ java -jar selenium-server-standalone-3.11.0.jar -role node -port 5555 -hub http://192.168.2.41:4444/grid/register

# http://localhost:4444/grid/console
# id : http://192.168.157.130:5555, OS : LINUX
# id : http://192.168.91.1:5556, OS : mixed OS  # VMware Network Adapter VMnet1(192.168.91.1)
# id : http://192.168.91.1:5557, OS : mixed OS  # VMware Network Adapter VMnet1(192.168.91.1)	
