#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import conf
import psycopg2
import xml.etree.ElementTree as ET
from datetime import datetime

try:
    conn = psycopg2.connect(
        user=conf.pg_db_user,
        password=conf.pg_db_pwd,
        host=conf.pg_db_host,
        database=conf.pg_db_name)
    cur = conn.cursor()

    f = ET.parse('data/sample_03.xml')
    for i in f.findall('food'):
        c = [i.find(n).text for n in ('item', 'price', 'description',
                                      'calories')]
        sql = "insert into github.sample_03 (item, price, description,\
            calories) values ('" + c[0] + "', " + c[1] + ", '" + c[2] + "',\
                              '" + c[3] + "')"
        print(sql)
        cur.execute(sql)
        conn.commit()

except psycopg2.Error as e:
    dt = datetime.now().strftime('%Y%m%d %H:%M:%S.%f | ')
    f_path = os.path.expanduser('~/.logs/python-by-example.log')
    app_name = os.path.basename(__file__)
    with open(f_path, 'a') as f:
        f.write(dt + app_name + ' | ' + 'Exception Error: ' + str(e) + '\n')
    print('Exception Error: ' + str(e))
    cur.close
    conn.close()
    sys.exit(1)

except Exception as e:
    dt = datetime.now().strftime('%Y%m%d %H:%M:%S.%f | ')
    f_path = os.path.expanduser('~/.logs/python-by-example.log')
    app_name = os.path.basename(__file__)
    with open(f_path, 'a') as f:
        f.write(dt + app_name + ' | ' + 'Exception Error: ' + str(e) + '\n')
    print('Exception Error: ' + str(e))
    cur.close
    conn.close()
    sys.exit(1)

else:
    dt = datetime.now().strftime('%Y%m%d %H:%M:%S.%f | ')
    f_path = os.path.expanduser('~/.logs/python-by-example.log')
    app_name = os.path.basename(__file__)
    with open(f_path, 'a') as f:
        f.write(dt + app_name + ' | ' + 'Successfully Executed...\n')
    print('Successfully Executed...')
    cur.close
    conn.close()
    sys.exit(0)
