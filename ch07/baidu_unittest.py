#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class BaiduTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu(self):
        print('test_baidu')
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium ide")
        driver.find_element_by_id("su").click()

    def is_element_present(self, how, what):
        print('is_element_present')
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    
    def test_is_element_present(self):
        driver = self.driver
        driver.get(self.base_url)
        self.assertTrue(self.is_element_present(By.ID, "kw"), msg='not present')
        
    def is_alert_present(self):
        print('is_alert_present')
        try:
            alert = self.driver.switch_to.alert
            print(alert.text)
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        print('close_alert_and_get_its_text')
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def test_alert_and_its_text(self):
        print('test_alert_and_its_text')
        self.open_alert()
        text = self.close_alert_and_get_its_text()
        print(text)
        self.assertTrue(text)

    def test_is_alert_present(self):
        print('test_is_alert_present')
        self.open_alert()
        self.assertTrue(self.is_alert_present())

    def open_alert(self):
        # print('open_alert')
        driver = self.driver
        driver.get(self.base_url)
        links = driver.find_elements_by_link_text('设置')
        ActionChains(driver).move_to_element(links[1]).perform()
        # 打開搜索設置
        driver.find_element_by_class_name('setpref').click()
        # 保存設置
        # driver.find_element_by_css_selector('#gxszButton > a.prefpanelgo').click()
        # use WebDriverWait and EC.element_to_be_clickable to fix 'Element <a class="prefpanelgo" href="#"> could not be scrolled into view'
        element = WebDriverWait(driver, 5, 0.5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#gxszButton > a.prefpanelgo'))
        )
        element.click() # if we comment this,it will not trigger alert and raise NoAlertPresentException
        time.sleep(1)

    def tearDown(self):
        # time.sleep(5)
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
