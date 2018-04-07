#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from time import sleep
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#鼠标悬停相“设置”链接
# link = driver.find_element_by_link_text('设置')
links = driver.find_elements_by_link_text('设置')
for link in links:
    print(link.text)
    print(link.get_attribute("name"))
ActionChains(driver).move_to_element(links[1]).perform()
# 打開搜索設置
driver.find_element_by_class_name('setpref').click()


# 保存設置
# driver.find_element_by_css_selector('#gxszButton > a.prefpanelgo').click()
# use WebDriverWait and EC.element_to_be_clickable to fix 'Element <a class="prefpanelgo" href="#"> could not be scrolled into view'
element = WebDriverWait(driver, 5, 0.5).until(
    # EC.presence_of_element_located((By.CSS_SELECTOR, '#gxszButton > a.prefpanelgo'))
    
    # change to element_to_be_clickable because of selenium.common.exceptions.ElementNotInteractableException: Message: Element
    # <a class="prefpanelgo" href="#"> could not be scrolled into view
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gxszButton > a.prefpanelgo'))
)
print(element.get_attribute('outerHTML'))
print(element.get_attribute('class'))
# sleep(1)
# driver.maximize_window()
element.click()

sleep(1)

#接收弹窗
# driver.switch_to.alert.accept()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()


# driver.quit()

