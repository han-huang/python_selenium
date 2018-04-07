#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
#定義檔目錄
# result_dir = 'C:\\Users\\Han\\selenium_test\\ch08\\reports'
result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports", "example_suite")
print(__file__)
print('os.path.dirname(__file__) %s' % os.path.dirname(__file__))
print('os.path.abspath(__file__) %s' % os.path.abspath(__file__))
print('os.path.dirname(os.path.abspath(__file__)) %s' % os.path.dirname(os.path.abspath(__file__)))

print('result_dir %s' % result_dir)

lists = os.listdir(result_dir)
#重新按時間對目錄下的檔進行排列
lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
print('最新的文件為： ' + lists[-1])
file = os.path.join(result_dir, lists[-1])
print(file)


# >>> result_dir = "C:\\Users\\Han\\selenium_test\\ch08\\reports\\example_suite"
# >>> import os
# >>> os.listdir(result_dir)
# ['Test_test_baidu.MyTest_2018-03-26_01-19-26.html', 'Test_test_baidu.MyTest_2018-03-27_15-47-55.html', 'Test_test_youdao.MyTest_2018-03-26_01-19-26.html', 'Test_test_youdao.MyTest_2018-03-27_15-47-55.html']

