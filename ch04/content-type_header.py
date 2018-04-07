#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://selenium-python.readthedocs.io/faq.html?highlight=firefoxprofile#how-to-auto-save-files-using-custom-firefox-profile
# To identify the content type you want to download automatically, you can use curl:
# curl -I URL | grep "Content-Type"
# https://zh.wikipedia.org/wiki/CURL

# Another way to find content type is using the requests module
import requests
headers = requests.head('http://www.python.org').headers
print(headers)
print()
headers = requests.head('https://tw.yahoo.com').headers
print(headers)
print(headers['content-type'])

