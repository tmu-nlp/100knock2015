#!/usr/bin/python
# _*_ coding:utf-8 _*_

import json
from pymongo import MongoClient
import sys

def main():
    client = MongoClient("localhost", 27017)
    db     = client.test # "test"というデータベースを取得
    col    = db.artist      # "artist"というコレクションを取得
    artist_file = open(sys.argv[1], "r")
    for line in artist_file:
        jsondict = json.loads(line.strip())
        col.insert(jsondict)
        

    artist_file.close()

if __name__=="__main__":
   main()
