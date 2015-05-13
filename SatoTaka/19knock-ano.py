#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from operator   import itemgetter
from collections import defaultdict

yomikomi = open(sys.argv[1], "r")

y_list = [line.strip().split("\t") for line in yomikomi] 
my_dict = defaultdict(lambda:0)

for each_list in y_list:
    my_dict[each_list[0]] += 1

l = len(y_list)

for word in my_dict:
    for index in range(l):
        if word in y_list[index][0]:
           y_list[index].append(my_dict[word])
for sentence in sorted(y_list, key = itemgetter(len(y_list[0])-1), reverse = True):
    print "\t".join(sentence[:-1])

for i,j in sorted(my_dict.items(), key = itemgetter(1), reverse = True):
    print i            
