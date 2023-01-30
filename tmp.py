import gzip
import shutil
import os
import glob

# with open('/opt/db/pgsql/inbound/sms-20220827000139.xml', 'rb') as f_in:
#     with gzip.open('/opt/db/pgsql/archive/sms-20220827000139.xml.gz', 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)


for f_path in glob.glob(os.path.join('/opt/db/pgsql/inbound/', 'sms-*.xml')):
    print('f_path: ' + f_path)
    with open(f_path, 'rb') as f:
        f_name = os.path.basename(f_path)
        print('f_name: ' + f_name)
        with gzip.open('/opt/db/pgsql/archive/' + f_name + '.gz', 'wb') as f_out:
            shutil.copyfileobj(f, f_out)
