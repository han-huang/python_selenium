#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep
import os


def output_source():
    with open(os.path.splitext(__file__)[0] + ".txt", mode='w', encoding='utf-8') as out_file:
        out_file.write(driver.page_source)


driver = webdriver.Firefox()
driver.set_window_size(1500, 1000)


# driver.get("https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_event_dblclick")
driver.get("http://api.jquery.com/dblclick/")



# default_frame = driver.switch_to.default_content()
# print("default_frame %s " % default_frame)

scrollHeight = driver.execute_script("return document.body.scrollHeight")
print(scrollHeight)
scrollHeight -= 1200
print(scrollHeight)


# http://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.execute_script
# https://stackoverflow.com/questions/47905232/python-selenium-message-element-not-visible
driver.execute_script("window.scrollTo(0, " + str(scrollHeight) + ");")

# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
# frame_now = driver.switch_to.frame(driver.find_element_by_tag_name('iframe')[0]) 
# print("frame_now %s " % frame_now)
# driver.switch_to.frame(0)
# driver.switch_to.default_content()

actions = ActionChains(driver)
# target = driver.find_element_by_xpath("//p[contains(text(), 'Double-click on this paragraph.')]")
# target = driver.find_element_by_class_name("dbl")
# target = driver.find_element_by_xpath('//div[@class="dbl"]')
# target = driver.find_element_by_xpath('/html/body/div')
# target = driver.find_element_by_css_selector('html>body>div')



# target = driver.find_element_by_class_name("div.code-demo>iframe>html>body>div")
# target = driver.find_element_by_class_name("div.code-demo")

target = driver.find_element_by_xpath('//div[@class="demo code-demo"]')
# target = driver.find_element_by_xpath('//span[@class="category"]')
# print(target.text)
print(target.location)
# sleep(2)
# actions.double_click(target).perform()
# actions.move_to_element_with_offset(target, 10, 20).perform()

# actions.move_to_element_with_offset(target, 50, 50).context_click().perform()
# sleep(1)
# actions.move_to_element_with_offset(target, 30, 30).click().perform()
# sleep(1)



# actions.move_to_element_with_offset(target, 30, 30).perform()
# sleep(1)
# print("double_click 1")
# try:
    # actions.double_click() # # work on firefox 59.0.1 (64 位元)
    # actions.perform()
# except:
    # print("exception")

sleep(1)
try:
    print("double_click 2")
    actions.move_to_element_with_offset(target, 30, 30).double_click().perform() # # work on firefox 59.0.1 (64 位元)
except:
    print("exception")

# sleep(1)
# actions.move_to_element_with_offset(target, 50, 50).context_click().perform()



# actions.key_down(Keys.TAB)
# actions.key_down(Keys.ARROW_DOWN)
# actions.key_down(Keys.ARROW_DOWN)
# actions.key_down(Keys.ARROW_DOWN)
# actions.key_down(Keys.ARROW_DOWN)
# actions.key_down(Keys.ARROW_DOWN)
# actions.key_down(Keys.ARROW_DOWN)
# actions.perform()
# sleep(1)
# actions.move_to_element_with_offset(target, 30, 30).double_click().perform()

# actions.move_by_offset(550, 450).perform()
# actions.click().click().perform()






# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
# scroll down
# print("scroll down")
# driver.execute_script("window.scrollTo(0, 600)") 

# def mouse_move(actions, target_li):
    # for i in range(len(target_li)):
        # ele = '//li[@data-tsource="' + target_li[i] + '"]'
        # target = driver.find_element_by_xpath(ele)
        # sleep(2)
        # print("move to %s" % target.text)
        # actions.move_to_element(target).perform()

# actions = ActionChains(driver)
# target_li = ['41012', '79150', '41011', '41013', '41010']
# mouse_move(actions, target_li)


# driver.quit()
