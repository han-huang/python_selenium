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
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return number*factorial(number-1)


# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch12\behave>behave factorial\features\third.feature
# Feature: Compute factorial # factorial/features/third.feature:1
  # In order to play with Lettuce
  # As beginners
  # We'll implement factorial
  # Scenario: Factorial of 0       # factorial/features/third.feature:6
    # Given I have the number 0    # factorial/features/steps/third.py:9
    # When I compute its factorial # factorial/features/steps/third.py:14
    # Then I see the number 1      # factorial/features/steps/third.py:20

  # Scenario: Factorial of 1       # factorial/features/third.feature:11
    # Given I have the number 1    # factorial/features/steps/third.py:9
    # When I compute its factorial # factorial/features/steps/third.py:14
    # Then I see the number 1      # factorial/features/steps/third.py:20

  # Scenario: Factorial of 2       # factorial/features/third.feature:16
    # Given I have the number 2    # factorial/features/steps/third.py:9
    # When I compute its factorial # factorial/features/steps/third.py:14
    # Then I see the number 2      # factorial/features/steps/third.py:20

  # Scenario: Factorial of 3       # factorial/features/third.feature:21
    # Given I have the number 3    # factorial/features/steps/third.py:9
    # When I compute its factorial # factorial/features/steps/third.py:14
    # Then I see the number 6      # factorial/features/steps/third.py:20

  # Scenario: Factorial of 4       # factorial/features/third.feature:26
    # Given I have the number 4    # factorial/features/steps/third.py:9
    # When I compute its factorial # factorial/features/steps/third.py:14
    # Then I see the number 24     # factorial/features/steps/third.py:20

# 1 feature passed, 0 failed, 0 skipped
# 5 scenarios passed, 0 failed, 0 skipped
# 15 steps passed, 0 failed, 0 skipped, 0 undefined
# Took 0m0.011s
		