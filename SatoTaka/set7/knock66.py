#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
from pymongo import MongoClient

def main():
    client = MongoClient("localhost", 27017)
    db = client.test
    col = db.artist

    print col.find({"area": "Japan"}).count()
    

if __name__=="__main__":
   main()
