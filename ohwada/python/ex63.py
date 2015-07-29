#!/usr/bin/python
# -*- coding:utf-8 -*-


from kyotocabinet import *
import sys
import json


def create_db(db_file, data_file):
    if not db.open(db_file, DB.OWRITER | DB.OCREATE):
        print >>sys.stderr, "open error: " + str(db.error())

    for line in open(data_file):
        dic = json.loads(line)
        if "tags" in dic:
            lst = []
            for tag in dic["tags"]:
                c = tag["count"]
                v = tag["value"]
                lst.append((c,v))
        db.set(dic["name"], lst)


if __name__ == "__main__":
    db = DB()
    #create_db("artist_tags.kch", "artist.json")
    if not db.open("artist_tags.kch", DB.OREADER):
        print >>sys.stderr, "open error: " + str(db.error())
    NAME = sys.argv[1]
    print db.get(NAME)

