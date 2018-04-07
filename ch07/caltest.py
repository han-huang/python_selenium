#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from calculator import Count
   
class TestCount:

    def test_add(self):
        try:
            j = Count(2, 3)
            # j = Count(2, 6)
            add = j.add()
            assert(add == 5), 'Interger addition result error!'
        except AssertionError as msg:
            print(msg)
        else:
            print('Test pass!')

mytest = TestCount()
mytest.test_add()
