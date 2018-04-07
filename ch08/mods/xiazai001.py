#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import getpass
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Xiazai001():

    def __init__(self):
        self.username = None
        self.pw = None
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("http://www.xiazai001.com/forum.php")

    def login(self):
        self.driver.find_element_by_id("ls_username").clear()
        # username = input("Enter your username:")
        self.username = getpass.getpass("Enter your username:")
        self.driver.find_element_by_id("ls_username").send_keys(self.username)
        
        self.driver.find_element_by_id("ls_password").clear()
        # self.pw = input("Enter your password:")
        self.pw = getpass.getpass("Enter your password:")
        self.driver.find_element_by_id("ls_password").send_keys(self.pw)
        
        self.driver.find_element_by_xpath('//button[@type="submit" and @tabindex="904"]').click()

        try:
            element = WebDriverWait(self.driver, 5, 0.5).until(
                EC.presence_of_element_located((By.XPATH,'//strong[@class="vwmy"]'))
            )
        except TimeoutException:
            print("login failed, try again !!!")
            self.login()
        else:
            print(element.text)

    def logout(self):
        try:
            element = WebDriverWait(self.driver, 5, 0.5).until(
                EC.presence_of_element_located((By.LINK_TEXT,'退出'))
            )
            # print(element)
            # print(type(element))
            print(element.text)
            element.click()
            # self.driver.quit()
        except:
            print("logout failed !!!")

def main():         
    test = Xiazai001()
    test.login()
    test.logout()

if __name__ == '__main__':
    main()
