#!usr/bin/python
#coding: utf-8
from pymongo import MongoClient
import json

client = MongoClient()
db = client.test
coll = db.artist
coll_dance = coll.find({'tags.value':'dance'})
count = 0
for i in coll_dance.sort('rating.count', 1):
	print i['name']
	count += 1
	if count ==	10:
		break
