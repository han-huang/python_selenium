#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.youdao.com/"

    def test_youdao(self):
        print('test_youdao')
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys("webdriver")
        driver.find_element_by_xpath("//button[contains(text(), '翻译')]").click()
        time.sleep(2)
        title = driver.title
        text ='【webdriver】什么意思_英语webdriver的翻译_音标_读音_用法_例句_在线翻译_有道词典'
        self.assertEqual(title, text)
        
    def tearDown(self):
        # self.driver.quit()
        pass

if __name__ == '__main__':
    unittest.main()
