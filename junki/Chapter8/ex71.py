#!usr/bin/python
#-*-coding:utf-8-*-

import sys

readfile = open(sys.argv[1])
stopwordfile = open(sys.argv[2])

wordlist = []
stoplist = []
for line in readfile:
	line = line.replace('.','')
	words = line.strip().split(" ")
	for word in words:
		wordlist.append(word)
print wordlist

for word in wordlist:
	for stopw in stopwordfile:	
		stopw = stopw.replace('\n','')
		stoplist.append(stopw)
print stoplist

for w in wordlist:
	for s in stoplist:
		if w in s:
		#	print w
			print 'true'
			continue
		else:
		#	print w
			print 'false'
			break