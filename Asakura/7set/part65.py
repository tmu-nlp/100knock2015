#usr/bin/python
#coding:utf-8

from pymongo import MongoClient
import sys


def main():
    client = MongoClient('localhost',27017)
    db = client['test']
    collection = db.artist
    for num,col in enumerate(collection.find({'name':'Queen'})):
        print num,col


if __name__== '__main__':
    main()
