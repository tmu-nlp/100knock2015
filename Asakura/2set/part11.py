#!usr/bin/python
#--*--coding:utf-8--*--

import sys

openfile = open(sys.argv[1],"r")

for line in openfile:
    line2 = line.split("\t")
    str1=" ".join(line2)
    print str1,
