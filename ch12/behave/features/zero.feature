Feature: Compute factorial
    In order to introduce Behave
    We calc factorial as example

    Scenario: Factorial of 0
        Given I have the number 0
        When I compute its factorial
        Then I see the number 1

		
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch12\behave>behave features\zero.feature
# Feature: Compute factorial # features/zero.feature:1
#   In order to introduce Behave
#   We calc factorial as example
#   Scenario: Factorial of zero    # features/zero.feature:5
#     Given I have the number 0    # features/steps/zero_steps.py:6
#     When I compute its factorial # features/steps/zero_steps.py:11
#     Then I see the number 1      # features/steps/zero_steps.py:17
#       Assertion Failed: Got -1



# Failing scenarios:
#   features/zero.feature:5  Factorial of zero

# 0 features passed, 1 failed, 0 skipped
# 0 scenarios passed, 1 failed, 0 skipped
# 2 steps passed, 1 failed, 0 skipped, 0 undefined
# Took 0m0.003s
		