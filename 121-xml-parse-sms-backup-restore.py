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


    tree = ET.parse('../../github-data/sms-lite-mms.xml')
    root = tree.getroot()

    for x in root:
        if x.tag == 'sms':
            print('sms')
            # sql = (root.tag, root.attrib['count'], root.attrib['backup_set'], root.attrib['backup_date'], root.attrib['type'], x.tag)
            sql = ("insert into github.xml_parse_ea_backup_restore_lnd (re_val,ra_count,ra_backup_set,ra_backup_date,ra_type,e_val,ea_protocol,ea_address,ea_date,ea_type,ea_subject,ea_body,ea_toa,ea_sc_toa,ea_service_center,ea_read,ea_status,ea_locked,ea_date_sent,ea_sub_id,ea_readable_date,ea_contact_name) values ('" + root.tag + "'," + root.attrib['count'] + ",'" + root.attrib['backup_set'] + "'," + root.attrib['backup_date'] + ",'" + root.attrib['type'] + "','" + x.tag + "'," + x.attrib['protocol'] + ",'" + x.attrib['address'] + "'," + x.attrib['date'] + "," + x.attrib['type'] + ",'" + x.attrib['subject'] + "','" + x.attrib['body'] + "','" + x.attrib['toa'] + "','" + x.attrib['sc_toa'] + "','" + x.attrib['service_center'] + "'," + x.attrib['read'] + "," + x.attrib['status'] + "," + x.attrib['locked'] + "," + x.attrib['date_sent'] + "," + x.attrib['sub_id'] + ",'" + x.attrib['readable_date'] + "','" + x.attrib['contact_name'] + "');")
        elif x.tag == 'mms':
            # sql = (root.tag, root.attrib['count'], root.attrib['backup_set'], root.attrib['backup_date'], root.attrib['type'], x.tag)
            # sql = (x.tag, x.attrib['date'], x.attrib['rr'], x.attrib['sub'], x.attrib['ct_t'], x.attrib['read_status'], x.attrib['seen'], x.attrib['msg_box'], x.attrib['address'], x.attrib['sub_cs'], x.attrib['resp_st'], x.attrib['retr_st'], x.attrib['d_tm'], x.attrib['text_only'], x.attrib['exp'], x.attrib['locked'], x.attrib['m_id'], x.attrib['st'], x.attrib['retr_txt_cs'], x.attrib['retr_txt'], x.attrib['creator'], x.attrib['date_sent'], x.attrib['read'], x.attrib['m_size'], x.attrib['rpt_a'], x.attrib['ct_cls'], x.attrib['pri'], x.attrib['sub_id'], x.attrib['tr_id'], x.attrib['resp_txt'], x.attrib['ct_l'], x.attrib['m_cls'], x.attrib['d_rpt'], x.attrib['v'], x.attrib['_id'], x.attrib['m_type'], x.attrib['readable_date'], x.attrib['contact_name'])
            sql = ("insert into github.xml_parse_ea_backup_restore_lnd (re_val,ra_count,ra_backup_set,ra_backup_date,ra_type,e_val,ea_date,ea_rr,ea_sub,ea_ct_t,ea_read_status,ea_seen,ea_msg_box,ea_address,ea_sub_cs,ea_resp_st,ea_retr_st,ea_d_tm,ea_text_only,ea_exp,ea_locked,ea_m_id,ea_st,ea_retr_txt_cs,ea_retr_txt,ea_creator,ea_m_size,ea_rpt_a,ea_ct_cls,ea_pri,ea_tr_id,ea_resp_txt,ea_ct_l,ea_m_cls,ea_d_rpt,ea_v,ea_id,ea_m_type,ea_readable_date,ea_contact_name) values ()")

            for p in root.findall('.//part'):
                if 'data' in p.attrib:
                    # data_val = p.attrib['text']
                    data_val = 'yes'
                else:
                    data_val = ''
                print(root.attrib['backup_set'], root.attrib['backup_date'], x.attrib['date'], x.attrib['address'], p.tag, p.attrib['seq'], p.attrib['ct'], p.attrib['name'], p.attrib['chset'], p.attrib['cd'], p.attrib['fn'], p.attrib['cid'], p.attrib['cl'], p.attrib['ctt_s'], p.attrib['ctt_t'], p.attrib['text'], data_val)

            for a in root.findall('.//addr'):
                address_val = a.attrib['address']
                type_val = a.attrib['type']
                charset_val = a.attrib['charset']
                print(root.attrib['backup_set'],root.attrib['backup_date'],x.tag,x.attrib['date'],x.attrib['date_sent'],x.attrib['address'],x.attrib['read'],x.attrib['locked'],x.attrib['readable_date'],x.attrib['contact_name'],p.tag,address_val,type_val,charset_val)

            # sql = (sql + sql_p + sql_a)
        else:
            break

        # sql = "insert into github.sample_03 (item, price, description, calories) values ('" + c[0] + "', " + c[1] + ", '" + c[2] + "', '" + c[3] + "')"
        # print(sql)
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
