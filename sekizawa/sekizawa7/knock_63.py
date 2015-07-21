#!usr/bin/python
#coding:utf-8

import sys
import json
import kyotocabinet as kc
import knock_60
import pickle

if __name__ == "__main__":
    db = knock_60.KyotoCabinet()
    db.open("artist2.kch", kc.DB.OWRITER | kc.DB.OCREATE)
    json_file = open("artist.json", "r")
    for line in json_file:
        line = line.decode("utf-8")
        data = json.loads(line)
        if "name" in data and "tags" in data:
#            tag_list = []
 #           for tag in data["tags"]:
  #              tag_list.append(tag[u"count"])
   #             tag_list.append(tag[u"value"])
    #        db.set(data["name"].encode("utf-8"), tag_list)
             db.set(data["name"].encode("utf-8"), pickle.dumps(data["tags"]))
    print (pickle.loads(db.get_str(sys.argv[1])))

    json_file.close()

