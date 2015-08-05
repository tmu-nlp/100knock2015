#!/usr/bin/python
# -*- coding:utf-8 -*-


from kyotocabinet import *
import sys
import json


db = DB()
if not db.open("artist_area.kch", DB.OREADER):
    print >>sys.stderr, "open error: " + str(db.error())


cur = db.cursor()
cur.jump()
c = 0
while True:
    rec= cur.get_str(True)
    if not rec:
        break
    elif rec[1] == "Japan":
        c += 1
cur.disable()

print c
