#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
import re

if __name__=="__main__":

    open_file = open(sys.argv[1], "r")

    category = re.compile("\[\[Category\:(.*)\]\]")

    for line in open_file:
        if category.search(line) is not None:
           print category.search(line).group(1)
