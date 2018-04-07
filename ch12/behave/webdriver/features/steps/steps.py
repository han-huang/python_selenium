#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from behave import given, when, then, step

@when('we visit google')
def step(context):
   context.browser.get('http://www.google.com')

@then('it should have a title "Google"')
def step(context):
   assert context.browser.title == "Google"

# https://testingbot.com/support/getting-started/python.html
   
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch12\behave>behave webdriver\features\google.feature
# Feature: Testing google # webdriver/features/google.feature:1

  # Scenario: visit google and check       # webdriver/features/google.feature:3
    # When we visit google                 # webdriver/features/steps/steps.py:5
    # Then it should have a title "Google" # webdriver/features/steps/steps.py:9

# 1 feature passed, 0 failed, 0 skipped
# 1 scenario passed, 0 failed, 0 skipped
# 2 steps passed, 0 failed, 0 skipped, 0 undefined
# Took 0m42.676s

		