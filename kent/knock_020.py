#!/usr/bin/python
#-*-coding:utf-8-*-

import json
<<<<<<< HEAD
f = open("jawiki-country.json", "r")
w = open("UK.txt", "w")

for line in f:
    line = line.strip()
    jsonData = json.loads(line)

    if jsonData["title"] == u"イギリス":
        print jsonData["text"].encode("utf-8")
        w.write(jsonData["text"].encode("utf-8"))
=======

f = open("jawiki-country.json", "r")

jsonData = json.load(f)

print json.dumps(jsonData, sort_keys = True, indent = 4)

f.close()
>>>>>>> d229748cdbdb801ed8849831272f0088934937ff
