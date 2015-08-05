#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import json

f = open("jawiki-country-revised.json", "r")

Data = json.load(f)

for a in Data:
    if a["title"] == u"イギリス":
        print a["text"].encode("utf-8")
        break


