#!/usr/bin/python
#-*-coding:utf-8-*-

import re

f = open("UK.txt", "r")
my_dict = {}

info = re.compile("\|(.*) = (.*)")
for line in f:
    i = info.search(line)
    if i is not None:
        print line,
        my_dict[i.group(1)] = i.group(2)

    for i, j in my_dict.items():
        print i + "=" + j
