#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from datetime import datetime

try:
    print('Hello World!')

except Exception as e:
    dt = datetime.now().strftime('%Y%m%d %H:%M:%S.%f | ')
    f_path = os.path.expanduser('~/.logs/python-by-example.log')
    app_name = os.path.basename(__file__)
    with open(f_path, 'a') as f:
        f.write(dt + app_name + ' | ' + 'Exception Error: ' + str(e) + '\n')
    print('Exception Error: ' + str(e))
    sys.exit(1)

else:
    dt = datetime.now().strftime('%Y%m%d %H:%M:%S.%f | ')
    f_path = os.path.expanduser('~/.logs/python-by-example.log')
    app_name = os.path.basename(__file__)
    with open(f_path, 'a') as f:
        f.write(dt + app_name + ' | ' + 'Successfully Executed...\n')
    print('Successfully Executed...')
    sys.exit(0)
