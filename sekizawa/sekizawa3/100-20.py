#!/usr/bin/python
#coding: utf-8

import json

if __name__ == "__main__":

    f = open("jawiki-country.json", "r")

    new = open("UK.json", "w") 
    for line in f:
        data = json.loads(line)
        if data["title"] == u"イギリス":
            new.write(data["text"].encode("utf-8"))

    f.close()
    new.close()


