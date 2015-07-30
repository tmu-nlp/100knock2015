#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
import re

if __name__=="__main__":

    open_file = open(sys.argv[1], "r")
    
    category = re.complie("ファイル:(.*?)/|")
    for line in open_file:
        match = category.search(ine)
        if match is not None:
           print match.group(1)
    open_file.close()
