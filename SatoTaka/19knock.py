#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from collections import defaultdict

yomikomi = open(sys.argv[1], "r")

my_list = [line.strip().split("\t")[0] for line in yomikomi]

my_dict = defaultdict(lambda: 0)

for index in range(len(my_list)):
    my_dict[my_list[index]] += 1

for prefecture, frequency in sorted(my_dict.items(), key = lambda x:x[1], reverse = True):
    print prefecture, frequency
