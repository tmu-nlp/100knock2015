#!usr/bin/python
#-*-coding:utf-8-*-

#python ex70.py rt-polarity.pos rt-polarity.neg
#vim sentiment.txt

import sys
import random

alllist = []

positive_file = open(sys.argv[1])
poscount = 0
poslist = []
for line in positive_file:
	line = '+1'+' '+line
	poslist.append(line.strip())
	#poslist.insert(0, "+1")
	poscount += 1

	#print " ".join(poslist), count


negative_file = open(sys.argv[2])
negcount = 0
neglist = []
for line in negative_file:
	line = '-1'+' '+line
	neglist.append(line.strip())#.split(" ")
	#neglist.insert(0, "-1")
	negcount += 1

	#print " ".join(neglist), count
neglist.extend(poslist)
random.shuffle(neglist)
writefile = open("sentiment.txt",'w')
for item in neglist:
	writefile.write(item+'\n')

print 'Positive Example ' + str(poscount)
print 'Negative Example ' + str(negcount)

