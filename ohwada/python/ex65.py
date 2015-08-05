#!/usr/bin/python
# -*- coding:utf-8 -*-

from pymongo import Connection

conn = Connection('localhost', 27017)
db = conn.test
coll = db.artist

for doc in coll.find({'name':'Queen'}):
    print repr(doc).decode('unicode-escape')
