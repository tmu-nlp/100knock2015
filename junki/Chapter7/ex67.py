#!usr/bin/python
#-*-coding:utf-8-*-

import sys

negative_file = open(sys.argv[1])

for line in negative_file:
	line = line.strip().split("\n")
	line = line.insert(0, "-1 ")
	print line