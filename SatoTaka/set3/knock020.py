#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import json

yomikomi = open(sys.argv[1], "r")

for line in yomikomi:
    line = line.strip()
    data = json.loads(line)
    if data["title"] == u"イギリス":
       print data["text"]#.encode("utf-8")


