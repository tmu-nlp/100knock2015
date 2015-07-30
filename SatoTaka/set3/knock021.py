#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import re

yomikomi = open(sys.argv[1], "r")

category = re.compile("\[\[Category\:.*\]\]")

for line in yomikomi:
    if category.search(line) is not None:
       print line.strip() 
