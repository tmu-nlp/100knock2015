#!usr/bin/python
#coding:utf-8

from pymongo import MongoClient

def main():
    client = MongoClient('localhost',27017)
    db = client['test']
    collection = db.artist
    for num,doc in enumerate(collection.find({'tags.value':'dance'}).sort('rating.count',1).limit(10)):
        print num,doc


if __name__== '__main__':
    main()
