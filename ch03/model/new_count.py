# -*- coding: utf-8 -*-
import sys
import os

# PACKAGE_PARENT = '..'
# SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
# print(SCRIPT_DIR)
# sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
# print(sys.path)

# print()
# print('__file__ %s' % __file__)
# print('os.path.expanduser(__file__) %s' % os.path.expanduser(__file__))
# print('os.getcwd() %s ' % os.getcwd())
# print('os.path.join(os.getcwd(), os.path.expanduser(__file__)) %s ' % os.path.join(os.getcwd(), os.path.expanduser(__file__)))
# print('os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))) %s ' % os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
# print('SCRIPT_DIR %s ' % SCRIPT_DIR)
# print('os.path.join(SCRIPT_DIR, PACKAGE_PARENT)) %s' % os.path.join(SCRIPT_DIR, PACKAGE_PARENT))
# print('os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)) %s '% os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
# print()


# sys.path.append('C:\\Users\\Han\\selenium_test\\ch03')
# sys.path.append('C:\\Users\\Han\\selenium_test\\ch03\\model')



# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
# You can expand your PYTHONPATH by applying more shorter and readable code snippet: 
# sys.path.append( os.path.join( os.path.dirname(__file__), os.path.pardir ) ) –

print()
print('os.path.dirname(__file__) %s ' % os.path.dirname(__file__))
print('os.path.pardir %s ' % os.path.pardir)
print('os.path.join(os.path.dirname(__file__), os.path.pardir) %s ' % os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
print()

from model.count import A
# from .count import A
# from count import A


# import sys
# from count import A

# from .count import A
# https://stackoverflow.com/questions/47878301/python-systemerror-parent-module-not-loaded-cannot-perform-relative-import
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch03>python -m model.new_count
# 7

# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch03\model>python new_count.py
# Traceback (most recent call last):
  # File "new_count.py", line 2, in <module>
    # from .count import A
# ModuleNotFoundError: No module named '__main__.count'; '__main__' is not a package

class B(A):

    def sub(self, a, b):
        return a - b

result = B().add(2, 5)
print(result)



# def main_load():
    # from count import A

# def module_load():
    # from .count import A
	
# if __name__ == '__main__':
    # pass
# else:
    # sys.path.append(".")
    # print(sys.path)

# def main():
    # from count import A
    # result = B().add(2, 5)
    # print(result)	

# if __name__ == '__main__':
    # from count import A
    # main()