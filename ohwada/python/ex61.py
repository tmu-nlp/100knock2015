#!/usr/bin/python
# -*- coding:utf-8 -*-

from kyotocabinet import *
import sys
import json


db = DB()
if not db.open("artist_area.kch", DB.OREADER):
    print >>sys.stderr, "open error: " + str(db.error())


NAME = sys.argv[1]
print db.get(NAME)

