#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
# driver.quit()



# 7.6. Desired Capabilities
# http://selenium-python.readthedocs.io/api.html?highlight=webdriver.Remote#desired-capabilities


# http://selenium-python.readthedocs.io/getting-started.html#using-selenium-with-remote-webdriver
# To use the remote WebDriver, you should have Selenium server running. To run the server, use this command:
# java -jar selenium-server-standalone-2.x.x.jar

# first to start selenium server -> java -jar selenium-server-standalone-3.11.0.jar
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch09>python remote_webdriver.py


# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>java -jar selenium-server-standalone-3.11.0.jar
# 01:03:34.804 INFO [GridLauncherV3.launch] - Selenium build info: version: '3.11.0', revision: 'e59cfb3'
# 01:03:34.804 INFO [GridLauncherV3$1.launch] - Launching a standalone Selenium Server on port 4444
# 2018-03-29 01:03:34.991:INFO::main: Logging initialized @543ms to org.seleniumhq.jetty9.util.log.StdErrLog
# 01:03:35.389 INFO [SeleniumServer.boot] - Welcome to Selenium for Workgroups....
# 01:03:35.390 INFO [SeleniumServer.boot] - Selenium Server is up and running on port 4444

# 01:42:58.307 INFO [ActiveSessionFactory.apply] - Capabilities are: Capabilities {browserName: chrome, version: }
# 01:42:58.309 INFO [ActiveSessionFactory.lambda$apply$11] - Matched factory org.openqa.selenium.remote.server.ServicedSession$Factory (provider: org.openqa.selenium.chrome.ChromeDriverService)
# Starting ChromeDriver 2.36.540470 (e522d04694c7ebea4ba8821272dbef4f9b818c91) on port 4686
# Only local connections are allowed.
# 01:43:00.692 INFO [ProtocolHandshake.createSession] - Detected dialect: OSS
# 01:43:00.933 INFO [RemoteSession$Factory.lambda$performHandshake$0] - Started new session 3e2e4bd1549c36bf5675726b7f4f4c8b (org.openqa.selenium.chrome.ChromeDriverService)
# 01:43:02.774 INFO [ActiveSessions$1.onStop] - Removing session 3e2e4bd1549c36bf5675726b7f4f4c8b (org.openqa.selenium.chrome.ChromeDriverService)
# 01:43:13.829 INFO [ActiveSessionFactory.apply] - Capabilities are: Capabilities {browserName: chrome, version: }
# 01:43:13.829 INFO [ActiveSessionFactory.lambda$apply$11] - Matched factory org.openqa.selenium.remote.server.ServicedSession$Factory (provider: org.openqa.selenium.chrome.ChromeDriverService)
# Starting ChromeDriver 2.36.540470 (e522d04694c7ebea4ba8821272dbef4f9b818c91) on port 44046
# Only local connections are allowed.
# 01:43:15.807 INFO [ProtocolHandshake.createSession] - Detected dialect: OSS
# 01:43:15.865 INFO [RemoteSession$Factory.lambda$performHandshake$0] - Started new session 3bd1e8e1f16e376c93e8dcedec40c552 (org.openqa.selenium.chrome.ChromeDriverService)
