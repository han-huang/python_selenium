#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import open
gd = {"c": 10}
with open("exec_a.py", "r") as f:
    exec(f.read(), gd)
    print(gd['a'])
    print(gd['b'])
