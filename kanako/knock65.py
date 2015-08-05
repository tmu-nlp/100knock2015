#!usr/bin/python
#coding: utf-8
from pymongo import MongoClient
import json

client = MongoClient()
db = client.test
coll = db.artist
for i in coll.find({'name':'Queen'}):
	print i
