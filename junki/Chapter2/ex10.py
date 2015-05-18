#!/usr/bin/python
#-*-coding:utf-8-*-
#行数カウントプログラム

import sys
text = open(sys.argv[1], "r")

count = 0

for line in text:
	count += 1
print count