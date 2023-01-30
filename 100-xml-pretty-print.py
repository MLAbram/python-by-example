#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.dom.minidom

dom = xml.dom.minidom.parse('data/calls-20220823000123.xml')
pretty_xml_as_string = dom.toprettyxml()

print(pretty_xml_as_string)
