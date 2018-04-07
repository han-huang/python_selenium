#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys, getpass, time
# sys.path.append("./models") # wrong
# sys.path.append("./page_obj") # wrong
from models import myunit, function
from page_obj.loginPage import Login

class LoginTest(myunit.MyTest):

    def user_login_verify(self, username='', pw=''):
        Login(self.driver).user_login(username, pw)

    def get_user_info(self):
        self.username = input("Enter your username:")
        self.pw = getpass.getpass("Enter your password:")

    def test_login1(self):
        self.get_user_info()
        self.user_login_verify(self.username, self.pw)
        lo = Login(self.driver)
        self.assertEqual(lo.login_success(), self.username)
        print(lo.login_success())
        png = 'user_pw_success_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
        function.insert_img(self.driver, png)
        lo.user_logout()

    def test_login2(self):
        self.user_login_verify()
        lo = Login(self.driver)
        text = lo.error_hint()
        print(text)
        self.assertEqual(lo.error_hint(), '抱歉，密碼空或包含非法字符')
        png = 'user_pw_empty_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
        function.insert_img(self.driver, png)

if __name__ == '__main__':
    unittest.main()

# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>python ch09\run_selenium-server.py
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>python ch11\test_case\login_sta.py
