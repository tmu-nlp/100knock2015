#!usr/bin/python
#-*-coding:utf-8-*-

import json
from pymongo import MongoClient
import sys

jsonfile = open(sys.argv[1])

client = MongoClient("localhost",27017)
database = client.test#
collection = database.artist

for line in jsonfile:
	jdict = json.loads(line.strip())
	database.collection.insert(jdict)
	