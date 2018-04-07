#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver


def main():         
    search_text = ['python', 'selenium', 'opencv']
    for text in search_text:
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get('http://www.baidu.com')
        driver.find_element_by_id('kw').send_keys(text) 
        driver.find_element_by_id('su').click()
        # driver.quit()

if __name__ == '__main__':
    main()
