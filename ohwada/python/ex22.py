#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import re


for line in open("article_uk.txt", "r"):
    m = re.search(r"\[\[Category:", line)
    if m is not None:
        line = line.strip().decode("utf-8")
        print line[m.end():-2]

    
