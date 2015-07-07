#!/usr/bin/python
# refa: http://shoken.hatenablog.com/entry/20120405/p1

import sys
import json
from pymongo import Connection
from pymongo import DESCENDING

if __name__ == "__main__":
    json_file = "artist.json"
    artist_data = open(json_file)

    connect = Connection()
    db = connect.nlp100_kodair
    col = db.json_dict
    exit()
    col.create_index([("tags.value", DESCENDING)])
    col.create_index([("aliases.name", DESCENDING)])
    col.create_index([("name", DESCENDING)])
    for line in artist_data:
        one_data = json.loads(line)
        col.insert(one_data)
     
