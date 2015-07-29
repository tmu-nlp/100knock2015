#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from pymongo import Connection

conn = Connection('localhost', 27017)
db = conn.test
coll = db.artist

from pymongo import DESCENDING

c = 0
for doc in coll.find({'tags.value':'dance'}).sort('rating.count', DESCENDING):
                                             # -1 と書いても同じ。デフォルトは ASCENDING
    print repr(doc).decode('unicode-escape')
    c += 1
    if c == 10:
        break


