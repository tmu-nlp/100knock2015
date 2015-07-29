#!/usr/bin/python
# -*- coding:utf-8 -*-

# JSON ファイルの内容をデータベースに入れる

from pymongo import Connection
import json

conn = Connection('localhost', 27017)
db = conn.test
coll = db.artist

for line in open('artist.json', 'r'):
    dic = json.loads(line)
    coll.insert(dic)


# インデックスをはる

from pymongo import ASCENDING

coll.create_index([('name', ASCENDING)])
coll.create_index([('aliases.name', ASCENDING)])
coll.create_index([('tags.value', ASCENDING)])
coll.create_index([('rating.value', ASCENDING)])

