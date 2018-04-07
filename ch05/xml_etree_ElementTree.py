#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://docs.python.org/3/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

# Or directly from a string:
# root = ET.fromstring(country_data_as_string)

print(root.tag)
print(root.attrib)
print()

for child in root:
    print(child.tag, child.attrib)
    print(type(child.attrib)) # <class 'dict'>
    print(child.attrib.keys())
    print(child.attrib['name'])
    print(child.attrib.values())
    print(child.attrib.items())
    print()

print(root[0][1].text)

# >>> d = {'Amy': (45, 60, 33), 'Bob': (50, 62, 78),
# ...      'Cathy': (62, 98, 87), 'David': (45, 22, 12),
# ...      'Eason': (63, 55, 71), 'Fred': (78, 79, 32)}
# >>> d.keys()
# dict_keys(['Amy', 'Bob', 'Cathy', 'David', 'Eason', 'Fred'])
# >>> d.values()
# dict_values([(45, 60, 33), (50, 62, 78), (62, 98, 87), (45, 22, 12), (63, 55, 71), (78, 79, 32)])
# >>> d.items()
# dict_items([('Amy', (45, 60, 33)), ('Bob', (50, 62, 78)), ('Cathy', (62, 98, 87)), ('David', (45, 22, 12)), ('Eason', (63, 55, 71)), ('Fred', (78, 79, 32))])
# >>>

# >>> for k in d.keys():
# ...     print(k)
# ...
# Amy
# Bob
# Cathy
# David
# Eason
# Fred
# >>>
