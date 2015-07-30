#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
import re
from collections import OrderedDict #格納した順番に整列される辞書

if __name__=="__main__":

    open_file = open(sys.argv[1], "r")
    mydict    = OrderedDict()
    category = re.compile("\|(.*) = (.*)")
    for line in open_file:
        match = category.search(line)
        if match is not None:
           mydict[match.group(1)] = match.group(2)
    
    for key,value in mydict.items():
        print key,value
