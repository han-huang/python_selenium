#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

# https://developer.mozilla.org/en-US/Firefox/Headless_mode


if __name__ == "__main__":
    options = Options()
    options.add_argument('-headless')
    driver = Firefox(executable_path='geckodriver', firefox_options=options)
    wait = WebDriverWait(driver, timeout=10)
    driver.get('http://www.google.com')
    wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
    wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
    print(driver.page_source)
    driver.quit()

# han@han-virtual-machine:~$ python3 firefox_headless_mode.py   # success
	
	
# /home/han/geckodriver.log
# 1522349823855	geckodriver	INFO	geckodriver 0.20.0
# 1522349823859	geckodriver	INFO	Listening on 127.0.0.1:39772
# 1522349824874	mozrunner::runner	INFO	Running command: "/usr/bin/firefox" "-marionette" "-headless" "-profile" "/tmp/rust_mozprofile.f5fcT8jyHJOg"
# *** You are running in headless mode.
# 1522349825436	Marionette	INFO	Enabled via --marionette
# 1522349826512	Marionette	INFO	Listening on port 34199
# 1522349826602	Marionette	WARN	TLS certificate errors will be ignored for this session
# *** UTM:SVC TimerManager:registerTimer called after profile-before-change notification. Ignoring timer registration for id: telemetry_modules_ping
# 1522349833830	geckodriver::marionette	ERROR	Failed to stop browser process	