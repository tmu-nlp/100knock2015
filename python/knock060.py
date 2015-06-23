# coding:utf-8
'''
python knock060.py ../Data/artist.json ../Data/result/knock060/python/db.kch
'''

import json
from kyotocabinet import *
import sys

db = DB()
if not db.open(sys.argv[2], DB.OWRITER | DB.OCREATE):
    print >>sys.stderr, "open error: " + str(db.error())

for line in open(sys.argv[1]):
    jdata = json.loads(line)
    if 'name' in jdata and 'area' in jdata:
        db.set(jdata['name'], jdata['area'])
    if u'name' in jdata and 'area' in jdata:
        db.set(jdata[u'name'], jdata['area'])

if not db.close():
    print >>sys.stderr, "close error: " + str(db.error())
