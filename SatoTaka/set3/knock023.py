#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
import re

if __name__=="__main__":

    open_file = open(sys.argv[1], "r")
    #open_fileはいただけない（リョースケ談）
    section   = re.compile("(=+)(.*)=+")
    for line in open_file:
        match = section.search(line)
        if match is not None:
           print "%s\t%d" % (match.group(2), len(match.group(1))-1)
    open_file.close()
