#!usr/bin/python
#coding: utf-8
from pymongo import MongoClient
import json

client = MongoClient()
db = client.test
coll = db.artist
count = 0
for i in coll.find({'aliases.name':'Silhouettes'}):
	print i
