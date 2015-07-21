#!usr/bin/local/python
#coding:utf-8

import json
from pymongo import MongoClient
from collections import defaultdict

if __name__ == "__main__":
    json_file = open("artist.json", "r")
    client = MongoClient('localhost', 27017)
    db = client.knock_database
    posts = db.posts

    for line in json_file:
        aliase_list = []
        tag_list = []
        data = json.loads(line)
        if "name" in data and "aliases" in data and \
           "tags" in data and "rating" in data:
            aliases = data["aliases"]
            tags = data["tags"]
            rating = data["rating"]
            for aliase in aliases:
                aliase_list.append(aliase["name"].encode("utf-8"))
            for tag in tags:
                tag_list.append(tag["value"].encode("utf-8"))
            data_dict = {"name": data["name"],\
                         "aliases_name": aliase_list,\
                         "tags_value": tag_list,\
                         "rating_value": rating["value"]}
            post_id = posts.insert(data_dict)

