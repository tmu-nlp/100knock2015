#usr/bin/python
#coding:utf-8

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    db = client.knock_database
    posts = db.posts
    art_dict = {}
    count = 0
    for post in posts.find({"tags_value":"dance"}):
        art_dict[post] = post["rating_value"]
    for key, value in sorted(art_dict.items(), key=lambda x:x[1], reverse = True):
        if count < 10:
            print key
            count += 1
        else:
            break


