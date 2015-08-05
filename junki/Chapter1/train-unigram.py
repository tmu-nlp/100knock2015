#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

my_dict = {}
total_count = 0

for line in open(sys.argv[1], "r"):
	words = line.split(" ")
	words.append("</s>")
	for word in words:
		my_dict[word] += 1
		total_count += 1
		
for word, count in total_count:
	probability = my_dict["words"] / total_count
	print "%s %f" % (word, probability)
		