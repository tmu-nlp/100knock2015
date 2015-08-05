#!/usr/bin/python
#-*-coding:utf-8-*-

from collections import defaultdict

my_file = open("hightemp.txt", "r")
word = defaultdict(str)
counts = {}

for line in my_file:
    words = line.strip().split("\t")
    print words
    if words[0] not in counts:
       counts[words[0]] = 1
    else:
       counts[words[0]] += 1
for key, value in sorted(counts.items(), key = lambda x:x[1], reverse = True):
    print key, value
