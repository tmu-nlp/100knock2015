#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import re


f = open("article_uk.txt", "r")
doc = f.read()

iterator = re.finditer(r"={2,4}.+", doc)
for val in iterator:
    string = val.group()
    output = string.strip("=").strip()
    if string[:4] == "====":
        print "\t" * 2 + output, 3
    elif string[:3] == "===":
        print "\t" + output, 2
    else:
        print output, 1

