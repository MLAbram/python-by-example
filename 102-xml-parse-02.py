#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et

mytree = et.parse('data/sms-20220823000123.xml')
myroot = mytree.getroot()

print(myroot)
print(myroot.tag)
print(myroot.tag[0:4])
print('myroot.attrib')
print(myroot.attrib)
print(myroot[0].tag)
print('')

for child in myroot:
    print(child.tag)

for child in myroot:
    print(child.tag, child.attrib)

# for x in myroot[0]:
#     print(x.tag, x.attrib)

# print('')

# for x in myroot[0]:
#     print(x.text)

# print('')

# for x in myroot.findall('smse'):
#     v_item = x.find('protocol').text
#     v_price = x.find('address').text
#     v_date = x.find('date').text
#     v_type = x.find('type').text
#     print(v_item, v_price, v_date, v_type)
