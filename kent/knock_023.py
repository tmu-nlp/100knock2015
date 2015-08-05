#!/usr/bin/python
#-*-coding:utf-8-*-

import re

f = open("UK.txt", "r")

section = re.compile("(==*).*==*")
for line in f:
    line = line.strip()
    if section.match(line) is not None:
        print line
        if section:
            print section.group(1)
