#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from pymongo import Connection

conn = Connection('localhost', 27017)
db = conn.test
coll = db.artist

AN = sys.argv[1]
for doc in coll.find({'aliases.name': AN}):
    print str(doc).decode('unicode-escape')
