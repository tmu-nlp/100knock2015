#!/usr/bin/python
# refa: http://shoken.hatenablog.com/entry/20120405/p1

import sys
import json
from pymongo import MongoClient
from pymongo import DESCENDING

if __name__ == "__main__":
    json_file = "artist.json"
    artist_data = open(json_file)

    client = MongoClient('localhost', 27017)
    db = client.nlp100
    col = db.json_dict
    col.create_index([("tags.value", DESCENDING)])
    col.create_index([("aliases.name", DESCENDING)])
    col.create_index([("name", DESCENDING)])
    exit()
    for line in artist_data:
        one_data = json.loads(line)
        db.json_dict.insert(one_data)
     
