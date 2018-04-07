#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://docs.python.org/3.0/library/xml.dom.minidom.html

from xml.dom import minidom
dom = minidom.parse('country_data.xml')
root = dom.documentElement

print(root.nodeName) # data
print(root.nodeValue) # None
print(root.nodeType) # 1
print(root.ELEMENT_NODE) # 1
print()
ranks = root.getElementsByTagName('rank')
print(ranks[0].tagName)
print(len(ranks))
print()
countries = root.getElementsByTagName('country')
print(countries[2].tagName)
print(len(countries))
print()
gdppcs = root.getElementsByTagName('gdppc')
print(gdppcs[1].tagName)
print(len(gdppcs))
print()
neighbors = root.getElementsByTagName('neighbor')
print(neighbors[1].tagName)
print(len(neighbors))
print()
neighbor_name=neighbors[0].getAttribute("name")
print(neighbor_name)
neighbor_direction=neighbors[0].getAttribute("direction")
print(neighbor_direction)
print()
neighbor_name=neighbors[3].getAttribute("name")
print(neighbor_name)
neighbor_direction=neighbors[3].getAttribute("direction")
print(neighbor_direction)
print()
g1=gdppcs[0].firstChild.data
print(g1)
g2=gdppcs[1].firstChild.data
print(g2)
