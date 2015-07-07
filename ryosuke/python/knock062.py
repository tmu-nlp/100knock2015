# coding:utf-8
'''
python knock062.py ../Data/result/knock060/python/db.kch
'''

import sys
from kyoto_cabinet_wrapper import *

db = KyotoCabinet()
db.open(sys.argv[1])

count = 0
for rec in db.cursor():
    if rec[1] == 'Japan':
        count += 1
print count
