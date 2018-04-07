#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page(object):

    target_url = 'http://www.hd.club.tw/portal.php'
    
    def __init__(self, selenium_driver, base_url=target_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        self.url = url
        print('self.url %s' % self.url)
        url = self.base_url + url
        print('url %s' % url)
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)
        
    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def wait_element(self, loc):
        return WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located(loc)
        )

if __name__ == '__main__':
    unittest.main()
