#!/usr/bin/env python
# -*- coding: utf-8 -*-

# with open('text.txt'.decode('utf-8'),'r') as f:
#     print f.read()

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import csv
import codecs

csvfile = file('csv_test.csv', 'wb')
csvfile.write(codecs.BOM_UTF8)
writer = csv.writer(csvfile, dialect='excel')
writer.writerow(['姓名'.encode('utf-8'), '年龄', '电话'])

data = [
    ('小河', '25', '1234567'),
    ('小芳', '18', '789456'),
    ('小李', '20', '6938287')
]
writer.writerows(data)

csvfile.close()

csvfile = file('csv_test.csv', 'rb')
reader = csv.reader(csvfile)

for line in reader:
    if line[0]=='小芳':
        # print line
        print '[%s]' % ', '.join(line)

csvfile.close()

writer=csv.writer(open('test.csv','wb'))
writer.writerow(['col1','col2','col3'])
data=[range(3) for i in range(10)]
for item in data:
    writer.writerow(item)