#!/usr/bin/python
# _*_ coding:utf-8 _*_ 

from pymongo import MongoClient

def main():
    client = MongoClient("localhost", 27017)
    db = client.test
    col = db.artist

    for document in  col.find({"aliases.name": "女王"}):
        print document


if __name__=="__main__":
   main()
