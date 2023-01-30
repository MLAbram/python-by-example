#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import xml.etree.ElementTree as ET
import datetime

try:
    # f = ET.parse('../../github-data/sms-lite.xml')
    # for i in f.findall('smses'):
    #     c = [i.find(n).text for n in ('protocol', 'address', 'date', 'type')]
    #     print(c)

    tree = ET.parse('../../github-data/calls-20220830000140.xml')
    root = tree.getroot()

    for x in root:
        if x.tag == 'call':
            print('call')
            # sql = (root.tag, root.attrib['count'], root.attrib['backup_set'], root.attrib['backup_date'], root.attrib['type'], x.tag)
            sql = ("insert into datasets.calls_backup_lnd (re_val,ra_count,ra_backup_set,ra_backup_date,ra_type,ea_val,ea_number,ea_duration,ea_date,ea_type,ea_presentation,ea_subscription_id,ea_post_dial_digits,ea_subscription_component_name,ea_readable_date,ea_contact_name)values(root.attrib['val'],root.attrib['count'],root.attrib['backup_set'],root.attrib['backup_date'],root.attrib['type'],x.attrib['val'],x.attrib['number'],x.attrib['duration'],x.attrib['date'],x.attrib['type'],x.attrib['presentation'],x.attrib['subscription_id'],x.attrib['post_dial_digits'],x.attrib['subscription_component_name'],x.attrib['readable_date'],x.attrib['contact_name']);")
        else:
            break

        # sql = "insert into github.sample_03 (item, price, description, calories) values ('" + c[0] + "', " + c[1] + ", '" + c[2] + "', '" + c[3] + "')"
        print(sql)
        print('The End...')

except Exception as e:
    dt = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S.%f | ')
    f_path = os.path.expanduser('~/.logs/python-by-example.log')
    app_name = os.path.basename(__file__)
    with open(f_path, 'a') as f:
        f.write(dt + app_name + ' | ' + 'Exception Error: ' + str(e) + '\n')
    print('Exception Error: ' + str(e))
    sys.exit(1)

else:
    dt = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S.%f | ')
    f_path = os.path.expanduser('~/.logs/python-by-example.log')
    app_name = os.path.basename(__file__)
    with open(f_path, 'a') as f:
        f.write(dt + app_name + ' | ' + 'Successfully Executed...\n')
    print('Successfully Executed...')
    sys.exit(0)
