#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# user_file = open('user_info.txt', 'r')
# values = user_file.readlines()
# user_file.close()
with open('user_info.txt', 'r') as user_file:
    values = user_file.readlines()
for serch in values:
    username = serch.split(',')[0]
    password = serch.split(',')[1]
    print(username, password)
