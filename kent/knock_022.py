#!usr/bin/python
#-*-coding:utf-8-*-

import re

f = open("UK.txt", "r")

category = re.compile("\[\[Category:(.*)\]\]")
for line in f:
    if category.search(line) is not None:
        print category.search(line).group(1)
