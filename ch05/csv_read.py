#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

data = csv.reader(open('info.csv', 'r'))
itb = iter(data) # Iterator
print(next(itb))
print()
for user in data:
    print('%-10s: %s' % (user[0], user[2]))

print()
print(type(data))
# itb = iter(data)
# print(next(itb)) # StopIteration
print()

# https://docs.python.org/3/library/csv.html

with open('info.csv', 'r') as fp:
    data = csv.reader(fp)
    for user in data:
        print('%12s: %s' % (user[0], user[2]))
    # print()
    # for user in data:
        # print('%-10s: %s' % (user[0], user[2]))