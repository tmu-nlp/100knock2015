#!usr/bin/python
#coding:utf-8


from pymongo import MongoClient


def main():
    client = MongoClient('localhost',27017)
    db = client['test']
    collection = db.artist
    for col in collection.find({'aliases.name':'女王'}):
        print col
    print collection.find({'aliases.name':'女王'}).count()


if __name__ == '__main__':
    main()
