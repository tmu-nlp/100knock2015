#!/usr/bin/python
#-*-coding:utf-8-*-
#分割したい数を表示→行カウント→
import sys

param = sys.argv

print param[2]
count = 1

for line in open(sys.argv[1]):
	print line.strip()
	if count == int(param[2]):
		break
	count += 1