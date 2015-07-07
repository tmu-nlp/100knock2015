#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
from pymongo import MongoClient
import json

def main():
    client = MongoClient("localhost", 27017)
    db     = client.test
    col    = db.artist

    for document in  col.find({"name": "Queen"}):
        print document

if __name__ == "__main__":
   main()


