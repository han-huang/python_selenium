#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import getpass
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

class Page():

    login_url = 'http://www.xiazai001.com/forum.php'
    
    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == self.base_url
        
    def open(self):
        self.driver.get(self.base_url)
        assert self.on_page, 'did not land on {}'.format(self.base_url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

class PageOperations(Page):

    username_loc = (By.ID, "ls_username")
    password_loc = (By.ID, "ls_password")
    submit_loc = (By.XPATH, '//button[@type="submit" and @tabindex="904"]')
    name_loc = (By.XPATH, '//strong[@class="vwmy"]')
    logout_loc = (By.LINK_TEXT, '退出')

    # Actions
    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()

    def wait_element(self, loc):
        return WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located(loc)
        )

    def check_login(self, name):
        try:
            # text = self.driver.find_element(*self.name_loc).text
            # name_ele = WebDriverWait(self.driver, 5, 0.5).until(
                # EC.presence_of_element_located(self.name_loc)
            # )
            name_ele = self.wait_element(self.name_loc)
            name_text = name_ele.text
            assert(name_text == name), "name mismatch, login failed"     
            print(name_text)
        except:
            print("logout failed !!!")          
            raise

    def logout(self):
        try:
            # element = WebDriverWait(self.driver, 5, 0.5).until(
                # EC.presence_of_element_located(self.logout_loc)
            # )
            element = self.wait_element(self.logout_loc)
            print(element.text)
            element.click()
        except:
            print("logout failed !!!")          
            raise

def test_user_login(driver, username, password):
    login_page = PageOperations(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
    # sleep(2)
    login_page.check_login(username)
    return login_page

def main():
    try:
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        username = input("Enter your username:")
        pw = getpass.getpass("Enter your password:")
        page = test_user_login(driver, username, pw)
        page.logout()
    finally:
        # driver.close()
        driver.quit() # https://hk.saowen.com/a/47ecc995d3b8f4b5a3278c255829a6f7f5ec12ad1f3afd078e7d26265cdbf405

if __name__ == '__main__':
    main()
