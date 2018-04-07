#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from behave import given, when, then, step


# http://lettuce.it/tutorial/simple.html ; modify it to fit behave

# @step('I have the number (\d+)')
@step('I have the number {number:d}')
# def have_the_number(step, number):
def step_impl(context, number):
    context.number = number

@step('I compute its factorial')
# def compute_its_factorial(step):
def step_impl(context):
    context.number = factorial(context.number)

# @step('I see the number (\d+)')
@step('I see the number {expected:d}')
# def check_number(step, expected):
def step_impl(context, expected):
    expected = int(expected)
    assert context.number == expected, \
        "Got %d" % context.number

def factorial(number):
    return -1
    # return 1

# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch12\behave>behave features\zero.feature
# Feature: Compute factorial # features/zero.feature:1
  # In order to introduce Behave
  # We calc factorial as example
  # Scenario: Factorial of zero    # features/zero.feature:5
    # Given I have the number 0    # features/steps/zero_steps.py:6
    # When I compute its factorial # features/steps/zero_steps.py:11
    # Then I see the number 1      # features/steps/zero_steps.py:17
      # Assertion Failed: Got -1



# Failing scenarios:
  # features/zero.feature:5  Factorial of zero

# 0 features passed, 1 failed, 0 skipped
# 0 scenarios passed, 1 failed, 0 skipped
# 2 steps passed, 1 failed, 0 skipped, 0 undefined
# Took 0m0.002s

# --------------------------------------------------

# change to the following :

# def factorial(number):
    # return 1

# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch12\behave>behave features\zero.feature
# Feature: Compute factorial # features/zero.feature:1
  # In order to introduce Behave
  # We calc factorial as example
  # Scenario: Factorial of zero    # features/zero.feature:5
    # Given I have the number 0    # features/steps/zero_steps.py:6
    # When I compute its factorial # features/steps/zero_steps.py:11
    # Then I see the number 1      # features/steps/zero_steps.py:17

# 1 feature passed, 0 failed, 0 skipped
# 1 scenario passed, 0 failed, 0 skipped
# 3 steps passed, 0 failed, 0 skipped, 0 undefined
# Took 0m0.002s
