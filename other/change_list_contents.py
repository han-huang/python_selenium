#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference

# It is neither pass-by-value or pass-by-reference - it is call-by-object. See this, by Fredrik Lundh:
# http://effbot.org/zone/call-by-object.htm
# Here is a significant quote:
# "...variables [names] are not objects; they cannot be denoted by other variables or referred to by objects."

def try_to_change_list_contents(the_list):
    print('got', the_list)
    the_list.append('four')
    print('changed to', the_list)

outer_list = ['one', 'two', 'three']

print('before, outer_list =', outer_list)
try_to_change_list_contents(outer_list)
print('after, outer_list =', outer_list)

# Output:

# before, outer_list = ['one', 'two', 'three']
# got ['one', 'two', 'three']
# changed to ['one', 'two', 'three', 'four']
# after, outer_list = ['one', 'two', 'three', 'four']
