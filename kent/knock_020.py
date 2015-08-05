#!/usr/bin/python
#-*-coding:utf-8-*-

import json
f = open("jawiki-country.json", "r")
w = open("UK.txt", "w")

for line in f:
    line = line.strip()
    jsonData = json.loads(line)

    if jsonData["title"] == u"イギリス":
        print jsonData["text"].encode("utf-8")
        w.write(jsonData["text"].encode("utf-8"))
