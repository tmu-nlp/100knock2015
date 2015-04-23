#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from operator import itemgetter

yomikomi = open(sys.argv[1], "r")
my_list = []

for line in yomikomi:
    words_list = line.strip().split("\t")
  
    my_list.append(words_list)
  
for sentence in sorted(my_list, key = itemgetter(2)):
    print "\t".join(sentence) 
