#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import re


f = open("article_uk.txt", "r")
doc = f.read()

iterator = re.finditer(r"ファイル:[^|]+\|", doc)
# iterator = re.finditer(r"ファイル:.+\|", doc)
for val in iterator:
    line = val.group().decode("utf-8")
    print line[5:-1]
        

