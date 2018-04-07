# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver

# https://pypi.python.org/pypi/selenium
# Example 2:
# Selenium WebDriver is often used as a basis for testing web applications. 
# Here is a simple example uisng Python’s standard unittest library:

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
