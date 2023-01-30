#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import conf
import glob
import gzip
import shutil
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

    # write to log file
    dt = datetime.now().strftime('%Y%m%d %H:%M:%S.%f | ')
    l_path = os.path.expanduser('~/.logs/python-by-example.log')
    app_name = os.path.basename(__file__)
    with open(l_path, 'a') as lp:
        lp.write(dt + app_name + ' | ' + 'Starting Script...\n')
    lp.close()

    for f_path in glob.glob(os.path.join('/opt/db/pgsql/inbound/', 'calls-*.xml')):
        with open(f_path, 'rb') as f:
            f_name = os.path.basename(f_path)
            # file_name = os.path.splitext(f_name)[0]

            tree = ET.parse(f_path)
            root = tree.getroot()

            for x in root:
                if x.tag == 'call':
                    # root element and call
                    cur.execute("insert into datasets.calls_backup_lnd(re_val,ra_count,ra_backup_set,ra_backup_date,ra_type,ea_val,ea_number,ea_duration,ea_date,ea_type,ea_presentation,ea_subscription_id,ea_post_dial_digits,ea_subscription_component_name,ea_readable_date,ea_contact_name)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(root.tag,root.attrib['count'],root.attrib['backup_set'],root.attrib['backup_date'],root.attrib['type'],x.tag,x.attrib['number'],x.attrib['duration'],x.attrib['date'],x.attrib['type'],x.attrib['presentation'],x.attrib['subscription_id'],x.attrib['post_dial_digits'],x.attrib['subscription_component_name'],x.attrib['readable_date'],x.attrib['contact_name']))
                else:
                    break

                conn.commit()

            # compress and save to /opt/db/pgsql/archive/ls
            with gzip.open('/opt/db/pgsql/archive/' + f_name + '.gz', 'wb') as f_out:
                shutil.copyfileobj(f, f_out)

            # delete source files
            os.remove(f_path)

            # write to log file
            dt = datetime.now().strftime('%Y%m%d %H:%M:%S.%f | ')
            l_path = os.path.expanduser('~/.logs/python-by-example.log')
            app_name = os.path.basename(__file__)
            with open(l_path, 'a') as lp:
                lp.write(dt + app_name + ' | ' + 'Ingested ' + f_name + '...\n')
            lp.close()

except psycopg2.Error as e:
    dt = datetime.now().strftime('%Y%m%d %H:%M:%S.%f | ')
    l_path = os.path.expanduser('~/.logs/python-by-example.log')
    app_name = os.path.basename(__file__)
    with open(l_path, 'a') as lp:
        lp.write(dt + app_name + ' | ' + 'Exception Error: ' + str(e) + '\n')
    print('Exception Error: ' + str(e))
    cur.close
    conn.close()
    f.close()
    lp.close()
    sys.exit(1)

except Exception as e:
    dt = datetime.now().strftime('%Y%m%d %H:%M:%S.%f | ')
    l_path = os.path.expanduser('~/.logs/python-by-example.log')
    app_name = os.path.basename(__file__)
    with open(l_path, 'a') as lp:
        lp.write(dt + app_name + ' | ' + 'Exception Error: ' + str(e) + '\n')
    print('Exception Error: ' + str(e))
    cur.close
    conn.close()
    f.close()
    lp.close()
    sys.exit(1)

else:
    dt = datetime.now().strftime('%Y%m%d %H:%M:%S.%f | ')
    l_path = os.path.expanduser('~/.logs/python-by-example.log')
    app_name = os.path.basename(__file__)
    with open(l_path, 'a') as lp:
        lp.write(dt + app_name + ' | ' + 'Successfully Executed...\n')
    print('Successfully Executed...')
    cur.close
    conn.close()
    f.close()
    lp.close()
    sys.exit(0)
