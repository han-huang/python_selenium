# -*- coding: utf-8 -*-
# from model import new_count
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch03>python test.py
# 9
# Traceback (most recent call last):
  # File "test.py", line 2, in <module>
    # from model import new_count
  # File "C:\Users\Han\selenium_test\ch03\model\new_count.py", line 2, in <module>
    # from count import A
# ImportError: cannot import name 'A'

# import sys
# sys.path.append("./model")
# sys.path.append("C:\\Users\\Han\\selenium_test\\ch03\\model")
# print(sys.path)
# sys.path.append("/C/Users/Han/selenium_test/ch03/model")
# from model.count import A

# import sys
# sys.path.append('C:\\Users\\Han\\selenium_test\\ch03')
# sys.path.append('C:\\Users\\Han\\selenium_test\\ch03\\model')

from model import new_count

test = new_count.B()
test.add(2, 5)

# from model import count
# test = count.A()
# print(test.add(2, 5))
