#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://pillow.readthedocs.io/en/3.1.x/reference/Image.html

from PIL import Image
im = Image.open("test.jpg")
im.rotate(45).show()

