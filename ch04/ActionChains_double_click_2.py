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

driver.execute_script("window.scrollTo(0, " + str(scrollHeight) + ");")

driver.switch_to.frame(0)
# driver.switch_to.default_content()

output_source()


actions = ActionChains(driver)


# sleep(2)
target = driver.find_element_by_xpath('/html/body/div')
# target = driver.find_element_by_css_selector('html>body>div') # ok
print(target.text)
print(target.location)

# sleep(1)
# actions.move_to_element_with_offset(target, 10, 20).double_click().perform()

sleep(1)
actions.double_click(target).perform() # work on firefox 59.0.1 (64 位元)


# actions.move_to_element_with_offset(target, 50, 50).context_click().perform()
# sleep(1)
# actions.move_to_element_with_offset(target, 30, 30).click().perform()
# sleep(1)
# actions.move_to_element_with_offset(target, 30, 30).perform()
# sleep(1)
# print("double_click")
# try:
    # actions.double_click()
    # actions.perform()
# except:
    # print("exception")

# sleep(1)

# try:
    # print("double_click")
    # actions.move_to_element_with_offset(target, 30, 30).double_click().perform()
# except:
    # print("exception")

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






# driver.quit()
