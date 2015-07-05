#usr/bin/python
#coding:utf-8

from pymongo import MongoClient
import sys


def main():
    client = MongoClient('localhost',27017)
    db = client['test']
    collection = db.artist
    print collection.find({'area':'Japan'}).count()
if __name__== '__main__':
    main()
