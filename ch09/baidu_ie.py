#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

# driver = webdriver.Ie('C:\\Users\\Han\\Anaconda3\\Library\\bin\\IEDriverServer.exe')
driver = webdriver.Ie()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
sleep(1)
driver.quit()


# https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver

# download - IEDriverServer_Win32_3.11.1.zip:
# http://selenium-release.storage.googleapis.com/index.html


# 把 IEDriverServer.exe 複製到 Path 的路徑其中之一

# 這裡複製到 C:\Users\Han\Anaconda3\Library\bin 目錄裡


# https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver#required-configuration

# Required Configuration

# The IEDriverServer exectuable must be downloaded and placed in your PATH.
# On IE 7 or higher on Windows Vista or Windows 7, you must set the Protected Mode settings for each zone to be the same value. The value can be on or off, as long as it is the same for every zone. To set the Protected Mode settings, choose "Internet Options..." from the Tools menu, and click on the Security tab. For each zone, there will be a check box at the bottom of the tab labeled "Enable Protected Mode".

# Additionally, "Enhanced Protected Mode" must be disabled for IE 10 and higher. This option is found in the Advanced tab of the Internet Options dialog.

# The browser zoom level must be set to 100% so that the native mouse events can be set to the correct coordinates.

# For Windows 10, you also need to set "Change the size of text, apps, and other items" to 100% in display settings.

# For IE 11 only, you will need to set a registry entry on the target computer so that the driver can maintain a connection to the instance of Internet Explorer it creates. For 32-bit Windows installations, the key you must examine in the registry editor is HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE. For 64-bit Windows installations, the key is HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE. Please note that the FEATURE_BFCACHE subkey may or may not be present, and should be created if it is not present. Important: Inside this key, create a DWORD value named iexplore.exe with the value of 0.

# ms-dos cmd: regedit
# 電腦\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE




# Selenium WebDriver typing very slow in text field on IE browser

# https://stackoverflow.com/questions/27985300/selenium-webdriver-typing-very-slow-in-text-field-on-ie-browser

# My issue was also with the driver architecture, and fixed it by downloading and using a 32bit one. The thread that helped me resolve

# http://forumsqa.com/question/typing-too-slow-in-text-fields-while-replaying-tests/

