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

    for f_path in glob.glob(os.path.join('/opt/db/pgsql/inbound/', 'sms-*.xml')):
        with open(f_path, 'rb') as f:
            f_name = os.path.basename(f_path)
            # file_name = os.path.splitext(f_name)[0]

            tree = ET.parse(f_path)
            root = tree.getroot()

            for x in root:
                if x.tag == 'sms':
                    # root element and sms
                    cur.execute("insert into github.sms_backup_lnd (re_val,ra_count,ra_backup_set,ra_backup_date,ra_type,ea_val,ea_protocol,ea_address,ea_date,ea_type,ea_subject,ea_body,ea_toa,ea_sc_toa,ea_service_center,ea_read,ea_status,ea_locked,ea_date_sent,ea_sub_id,ea_readable_date,ea_contact_name,aud_src_nm)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(root.tag,root.attrib['count'],root.attrib['backup_set'],root.attrib['backup_date'],root.attrib['type'],x.tag,x.attrib['protocol'],x.attrib['address'],x.attrib['date'],x.attrib['type'],x.attrib['subject'],x.attrib['body'],x.attrib['toa'],x.attrib['sc_toa'],x.attrib['service_center'],x.attrib['read'],x.attrib['status'],x.attrib['locked'],x.attrib['date_sent'],x.attrib['sub_id'],x.attrib['readable_date'],x.attrib['contact_name'],f_name))
                elif x.tag == 'mms':
                    # root element and mms
                    cur.execute("insert into github.sms_backup_lnd (re_val,ra_count,ra_backup_set,ra_backup_date,ra_type,ea_val,ea_date,ea_date_sent,ea_address,ea_read,ea_locked,ea_readable_date,ea_contact_name,ea_rr,ea_sub,ea_ct_t,ea_read_status,ea_seen,ea_msg_box,ea_sub_cs,ea_resp_st,ea_retr_st,ea_d_tm,ea_text_only,ea_exp,ea_m_id,ea_st,ea_retr_txt_cs,ea_retr_txt,ea_creator,ea_m_size,ea_rpt_a,ea_ct_cls,ea_pri,ea_tr_id,ea_resp_txt,ea_ct_l,ea_m_cls,ea_d_rpt,ea_v,ea_id,ea_m_type,aud_src_nm)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(root.tag,root.attrib['count'],root.attrib['backup_set'],root.attrib['backup_date'],root.attrib['type'],x.tag,x.attrib['date'],x.attrib['date_sent'],x.attrib['address'],x.attrib['read'],x.attrib['locked'],x.attrib['readable_date'],x.attrib['contact_name'],x.attrib['rr'],x.attrib['sub'],x.attrib['ct_t'],x.attrib['read_status'],x.attrib['seen'],x.attrib['msg_box'],x.attrib['sub_cs'],x.attrib['resp_st'],x.attrib['retr_st'],x.attrib['d_tm'],x.attrib['text_only'],x.attrib['exp'],x.attrib['m_id'],x.attrib['st'],x.attrib['retr_txt_cs'],x.attrib['retr_txt'],x.attrib['creator'],x.attrib['m_size'],x.attrib['rpt_a'],x.attrib['ct_cls'],x.attrib['pri'],x.attrib['tr_id'],x.attrib['resp_txt'],x.attrib['ct_l'],x.attrib['m_cls'],x.attrib['d_rpt'],x.attrib['v'],x.attrib['_id'],x.attrib['m_type'],f_name))
                    # mms parts
                    for p in root.findall('.//part'):
                        if 'data' in p.attrib:
                            data_val = p.attrib['text']
                        else:
                            data_val = ''
                        cur.execute("insert into github.sms_backup_mms_parts_lnd (ra_backup_set,ra_backup_date,ea_val,ea_date,ea_date_sent,ea_address,ea_read,ea_locked,ea_readable_date,ea_contact_name,eap_val,eap_seq,eap_ct,eap_name,eap_chset,eap_cd,eap_fn,eap_cid,eap_cl,eap_ctt_s,eap_ctt_t,eap_text,eap_data,aud_src_nm)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(root.attrib['backup_set'],root.attrib['backup_date'],x.tag,x.attrib['date'],x.attrib['date_sent'],x.attrib['address'],x.attrib['read'],x.attrib['locked'],x.attrib['readable_date'],x.attrib['contact_name'],p.tag,p.attrib['seq'],p.attrib['ct'],p.attrib['name'],p.attrib['chset'],p.attrib['cd'],p.attrib['fn'],p.attrib['cid'],p.attrib['cl'],p.attrib['ctt_s'],p.attrib['ctt_t'],p.attrib['text'],data_val,f_name))
                    # mms addrs
                    for a in root.findall('.//addr'):
                        address_val = a.attrib['address']
                        type_val = a.attrib['type']
                        charset_val = a.attrib['charset']
                        cur.execute("insert into github.sms_backup_mms_addrs_lnd (ra_backup_set,ra_backup_date,ea_val,ea_date,ea_date_sent,ea_address,ea_read,ea_locked,ea_readable_date,ea_contact_name,eaa_val,eaa_address,eaa_type,eaa_charset,aud_src_nm)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(root.attrib['backup_set'],root.attrib['backup_date'],x.tag,x.attrib['date'],x.attrib['date_sent'],x.attrib['address'],x.attrib['read'],x.attrib['locked'],x.attrib['readable_date'],x.attrib['contact_name'],p.tag,address_val,type_val,charset_val,f_name))
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
