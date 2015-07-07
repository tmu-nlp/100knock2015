#!usr/bin/python
#-*-coding:utf-8-*-
#python ex71_2.py stop_word.txt in.txt ←成功
#python ex71_2.py stop_word.txt accuracy.txt　←失敗		

import sys

count = 0
stopwordfile = open(sys.argv[1])
wordtext = open(sys.argv[2])
for line in wordtext:
	line = line.strip()#splitはしない

	for word in stopwordfile: 
		word = word.strip()
		if word == line:
			print 'true'
			count += 1
			break
		else:
			continue

if count == 0:
	print 'false'
		