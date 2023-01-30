#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# https://www.edureka.co/blog/python-xml-parser-tutorial/#:~:text=the%20upcoming%20examples.-,Python%20XML%20Parsing%20Modules,of%20that%20particular%20XML%20file.
#

import xml.etree.ElementTree as et

mytree = et.parse('../../github-data/calls-20220830000140.xml')
myroot = mytree.getroot()

print(myroot)
print(myroot.tag)
# print(myroot.tag[0:4])
# print(myroot.attrib)
# print(myroot[0].tag)
# print(myroot[12].tag)
# print('')

# for x in myroot[0]:
#     print(x.tag, x.attrib)

# print('')

# for x in myroot[0]:
#     print(x.text)

# print('')

# for x in myroot.findall('food'):
#     item = x.find('item').text
#     price = x.find('price').text
#     print(item, price)
