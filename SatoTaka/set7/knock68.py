#!/usr/bin/python
# _*_ coding:utf-8 _*_

from pymongo import MongoClient

def main():
    client = MongoClient("localhost", 27017)
    db = client.test # "test"というデータベースを取得してdbに格納
    col = db.artist  # "db(=test)というデータベースから、"artist"というコレクションを取得してcolに格納
    col2 = col.find({"tags.value": "dance"})

    for document in col2.sort({"rating.count": 1}):
        print document


if __name__=="__main__":
   main()
