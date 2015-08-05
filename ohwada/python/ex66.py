#!/usr/bin/python
# -*- coding:utf-8 -*-

from pymongo import Connection

conn = Connection('localhost', 27017)
db = conn.test
coll = db.artist

print coll.find({'area':'Japan'}).count()
# 22821
