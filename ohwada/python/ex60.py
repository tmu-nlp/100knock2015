#!/usr/bin/python
# -*- coding:utf-8 -*-

from kyotocabinet import *
import sys
import json


db = DB()
if not db.open("artist_area.kch", DB.OWRITER | DB.OCREATE):
    print >>sys.stderr, "open error: " + str(db.error())

for line in open("artist.json"):
    dic = json.loads(line)
    if "name" in dic and "area" in dic:
        db.set(dic["name"], dic["area"])


