Feature: Compute factorial
  In order to play with Lettuce
  As beginners
  We'll implement factorial

  Scenario: Factorial of 0
    Given I have the number 0
    When I compute its factorial
    Then I see the number 1

  Scenario: Factorial of 1
    Given I have the number 1
    When I compute its factorial
    Then I see the number 1

  Scenario: Factorial of 2
    Given I have the number 2
    When I compute its factorial
    Then I see the number 2

  Scenario: Factorial of 3
    Given I have the number 3
    When I compute its factorial
    Then I see the number 6

  Scenario: Factorial of 4
    Given I have the number 4
    When I compute its factorial
    Then I see the number 24


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