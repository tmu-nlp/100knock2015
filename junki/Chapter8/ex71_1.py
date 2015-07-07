#!usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

readfile = open(sys.argv[1])
stopwordfile = open(sys.argv[2])

for stopword in stopwordfile:
	stopword = stopword.replace('\n','')
	for word in readfile:
		word = word.replace('.','')
		match = re.search(stopword,word)

		if match is None:
			print word
			print 'Not match'
		else:
			print 'Match'