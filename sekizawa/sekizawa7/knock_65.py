#!usr/bin/local/python
#coding:utf-8

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    db = client.knock_database
    posts = db.posts

    for post in posts.find({"name": "Queen"}):
        print post

