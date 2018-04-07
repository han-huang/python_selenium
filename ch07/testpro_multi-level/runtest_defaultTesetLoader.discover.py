#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
# import testadd
# import testsub
# from testadd import TestAdd
# from testsub import TestSub

if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestAdd("test_add"))
    # suite.addTest(TestAdd("test_add_2"))
    # suite.addTest(TestSub("test_sub"))
    # suite.addTest(TestSub("test_sub_2"))
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)


# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch07\testpro_multi-level>python runtest_defaultTesetLoader.discover.py
# C:\Users\Han\selenium_test\ch07\testpro_multi-level\level_1\level_2\..\..
# test sub start
# test sub end
# .test sub start
# test sub end
# .test add start
# test add end
# .test add start
# test add end
# .
# ----------------------------------------------------------------------
# Ran 4 tests in 0.006s

# OK

# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch07\testpro_multi-level>python level_1\testadd.py
# test add start
# test add end
# .test add start
# test add end
# .
# ----------------------------------------------------------------------
# Ran 2 tests in 0.004s

# OK

# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch07\testpro_multi-level>python level_1\level_2\testsub.py
# level_1\level_2\..\..
# test sub start
# test sub end
# .test sub start
# test sub end
# .
# ----------------------------------------------------------------------
# Ran 2 tests in 0.002s

# OK
