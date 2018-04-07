#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
# from base import Page

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
from page_obj.base import Page

class Login(Page):

    url = '/'
    # index_login_loc = (By.XPATH, '//a[@href="member.php?mod=logging&amp;action=login"]') # get_attribute('href') - http://www.hd.club.tw/member.php?mod=logging&action=login
    # index_login_loc = (By.XPATH, '//a[contains(text(), "登錄")]')
    index_login_loc = (By.XPATH, '//a[contains(@href, "logging")]')
    # login_username_loc = (By.ID, 'username_Lnkpm') # id is different every time
    login_username_loc = (By.XPATH, '//input[contains(@id, "username_")]')
    # login_pw_loc = (By.ID, 'password3_Lnkpm') # id is different every time
    login_pw_loc = (By.XPATH, '//input[contains(@id, "password3_")]')
    login_button_loc = (By.NAME, 'loginsubmit')
    error_hint_loc = (By.CSS_SELECTOR, 'div.pc_inner')
    login_success_loc = (By.ID, 'myitem')
    logout_loc = (By.XPATH, '//a[contains(@href, "action=logout")]')

    def index_login(self):
        ele = self.find_element(*self.index_login_loc)
        print(ele.get_attribute('href'))
        ele.click()
        # eles = self.find_elements(*self.index_login_loc)
        # print(len(eles))
        # for ele in eles:
            # print(ele.get_attribute('href'))
        # actions = ActionChains(self.driver)
        # actions.move_to_element(ele).click().perform()

    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

        # current_window = self.driver.current_window_handle
        # all_handles = self.driver.window_handles
        # print(all_handles)
        # for handle in all_handles:
            # if handle != current_window:
                # self.driver.switch_to.window(handle)

        # div = self.find_element(By.ID, 'fwin_login')
        # print(div.get_attribute('id'))

    def login_pw(self, pw):
        self.find_element(*self.login_pw_loc).send_keys(pw)

    def login_btn(self):
        self.find_element(*self.login_button_loc).click()       
        
    def logout_btn(self):
        self.find_element(*self.logout_loc).click()     

    def user_login(self, username, pw):
        self.open()
        self.index_login()
        self.wait_element(self.login_username_loc)
        self.login_username(username)
        self.login_pw(pw)
        self.login_btn()

    def user_logout(self):
        ele =  self.login_success_ele()
        print('ele', ele.text)
        actions = ActionChains(self.driver)
        actions.move_to_element(ele).perform()
        self.logout_btn()

    def error_hint(self):
        self.wait_element(self.error_hint_loc)
        return self.driver.find_element(*self.error_hint_loc).text

    def login_success_ele(self):
        return self.driver.find_element(*self.login_success_loc)
        
    def login_success(self):
        return self.driver.find_element(*self.login_success_loc).text
