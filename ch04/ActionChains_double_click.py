#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep
import os
from selenium.webdriver.common.alert import Alert


def output_source():
    with open(os.path.splitext(__file__)[0] + ".txt", mode='w', encoding='utf-8') as out_file:
        out_file.write(driver.page_source)

driver = webdriver.Firefox()
driver.set_window_size(1500, 1000)



driver.get("https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_event_dblclick")
# driver.get("http://api.jquery.com/dblclick/")


# print(driver.window_handles)


# scrollHeight = driver.execute_script("return document.body.scrollHeight")
# print(scrollHeight)
# scrollHeight -= 1200
# print(scrollHeight)

# driver.execute_script("window.scrollTo(0, " + str(scrollHeight) + ");")


driver.switch_to.frame(0) # driver.switch_to.frame("iframeResult")


# script = '$' + '(\"p:contains(\'Double-click on this paragraph.\')\").dblclick();'
# print(script)
# driver.execute_script(script)

actions = ActionChains(driver)
target = driver.find_element_by_xpath("//p[contains(text(), 'Double-click on this paragraph.')]")
# target = driver.find_element_by_xpath("//p[text()='Double-click on this paragraph.']")


print(target.text)
print(target.location)


sleep(1)
actions.double_click(target).perform() # work on firefox 59.0.1 (64 位元)
sleep(1)

# print(Alert(driver).text)
# Alert(driver).accept()

try:
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
except:
    print("no alert to accept")


# actions.context_click(target).perform()
# actions.context_click().perform()
# actions.click().perform()
driver.switch_to.default_content()

output_source()





# target = driver.find_element_by_class_name("div.code-demo>iframe>html>body")
# target = driver.find_element_by_class_name("div.code-demo")


# target = driver.find_element_by_xpath('//div[@class="demo code-demo"]/iframe')
# target = driver.find_element_by_xpath('//span[@class="category"]')


# target = driver.find_element_by_xpath('//div[@class="demo code-demo"]/iframe')



# target = driver.find_element_by_xpath('//div[@class="demo code-demo"]')
# print(target.text)
# print(target.location)
# driver.switch_to.frame(target)

# sleep(2)

# target = driver.find_element_by_css_selector('html>body>div')
# print(target.text)
# print(target.location)
# actions.double_click(target).perform()

# sleep(2)
# actions.double_click().perform()

# actions.move_to_element_with_offset(target, 10, 20).perform()

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
