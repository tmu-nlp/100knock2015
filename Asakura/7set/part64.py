#!usr/bin/python
#coding:utf-8
import datetime
import sys
from pymongo import MongoClient
import json

def main():
    client = MongoClient('localhost',27017)
    db = client.test
    collection = db.artist
    for line in open('artist.json'):
        jdata = json.loads(line)
        collection.insert(jdata)




if __name__ == '__main__':
    main()
