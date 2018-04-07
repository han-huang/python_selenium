#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("http://www.youdao.com")
# 獲得cookie 資訊
cookie= driver.get_cookies()
#將獲得cookie 的資訊列印
print(cookie)
# driver.quit()


# Chrome:
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch04>python cookie.py

# DevTools listening on ws://127.0.0.1:12186/devtools/browser/58979053-c0ff-4873-8a88-d946ae68bbda
# [{'domain': '.youdao.com', 'expiry': 2467784831.528915, 'httpOnly': False, 'name': 'OUTFOX_SEARCH_USER_ID', 'path': '/', 'secure': False, 'value': '198115134@36.239.207.237'}, {'domain': '.youdao.com', 'httpOnly': False, 'name': 'DICT_UGC', 'path': '/', 'secure': False, 'value': 'be3af0da19b5c5e6aa4e17bd8d90b28a|'}, {'domain': '.youdao.com', 'httpOnly': False, 'name': 'JSESSIONID', 'path': '/', 'secure': False, 'value': 'abcSn_5e9Ull1-QJqRmjw'}, {'domain': 'www.youdao.com', 'httpOnly': False, 'name': '___rl__test__cookies', 'path': '/', 'secure': False, 'value': '1521704832004'}, {'domain': '.youdao.com', 'expiry': 1584776832, 'httpOnly': False, 'name': 'OUTFOX_SEARCH_USER_ID_NCOO', 'path': '/', 'secure': False, 'value': '225911006.15610877'}]

# Firefox:
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch04>python cookie.py
# [{'name': 'YOUDAO_MOBILE_ACCESS_TYPE', 'value': '1', 'path': '/', 'domain': '.youdao.com', 'expiry': 1553240882, 'secure': False, 'httpOnly': False}, {'name': 'DICT_UGC', 'value': 'be3af0da19b5c5e6aa4e17bd8d90b28a|', 'path': '/', 'domain': '.youdao.com', 'expiry': None, 'secure': False, 'httpOnly': False}, {'name': 'OUTFOX_SEARCH_USER_ID', 'value': '-2078985597@36.239.207.237', 'path': '/', 'domain': '.youdao.com', 'expiry': 2467784882, 'secure': False, 'httpOnly': False}, {'name': 'JSESSIONID', 'value': 'abc258lY2jH6w_NmDRmjw', 'path': '/', 'domain': '.youdao.com', 'expiry': None, 'secure': False, 'httpOnly': False}, {'name': '___rl__test__cookies', 'value': '1521704884032', 'path': '/', 'domain': 'www.youdao.com', 'expiry': None, 'secure': False, 'httpOnly': False}, {'name': 'OUTFOX_SEARCH_USER_ID_NCOO', 'value': '16061045.389608568', 'path': '/', 'domain': '.youdao.com', 'expiry': 1584776884, 'secure': False, 'httpOnly': False}]

