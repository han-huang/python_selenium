#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

print(__file__)
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.dirname(os.path.abspath(__file__)))



# https://github.com/dokelung/Python-QA/blob/master/questions/standard_lib/Python%20%E7%8D%B2%E5%8F%96%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%91%E5%8F%8A%E6%96%87%E4%BB%B6%E7%9B%AE%E9%8C%84(__file__%20%E7%9A%84%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95).md


# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch08>python test__file__.py
# test__file__.py

# C:\Users\Han\selenium_test\ch08\test__file__.py
# C:\Users\Han\selenium_test\ch08
# C:\Users\Han\selenium_test\ch08



# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>python ch08\test__file__.py
# ch08\test__file__.py
# ch08
# C:\Users\Han\selenium_test\ch08\test__file__.py
# C:\Users\Han\selenium_test\ch08
# C:\Users\Han\selenium_test\ch08




