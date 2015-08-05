#!usr/bin/python
#coding: utf-8
from pymongo import MongoClient
import json

client = MongoClient("localhost",27017)
db = client.test
coll = db.artist
for line in open("artist.json"):
	json_data = json.loads(line)
	coll.insert(json_data)
coll.create_index([('name',1)])
coll.create_index([('aliases.name',1)])
coll.create_index([('tags.value',1)])
coll.create_index([('rating.value',1)])
