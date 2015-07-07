#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
import json
import plyvel

def KVS(artist_file):
    
    kvs_database = plyvel.DB("data_base.ldb", create_if_missing = True)

    for line in artist_file:
        line = line.strip()
        jsondict = json.loads(line)
        kvs_database.put(jsondict.get("name", jsondict[u"name"]).encode("utf-8"), jsondict.get("area", "NONE").encode("utf-8"))
    return kvs_database

def main():
    
    artist_file  = open(sys.argv[1], "r")
    kvs_database = KVS(artist_file) 
    artist_file.close()

    for name, area in kvs_database:
        print name, area
    kvs_database.close()

if __name__ == "__main__":
   main()
