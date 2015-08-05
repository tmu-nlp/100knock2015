#!/usr/bin/python
#-*-coding:utf-8-*-

import re

f = open("UK.txt", "r")


#正規表現のとこから
mediafile = re.compile("http.*html")
for line in f:
    if mediafile.search(line) is not None:
        print line,
