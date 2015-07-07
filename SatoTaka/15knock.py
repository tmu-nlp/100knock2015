#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys

n = int(sys.argv[1])
yomikomi = open(sys.argv[2], "r")

my_list = [ line for line in yomikomi ]

index = len(my_list) - n

for i in range(index, len(my_list)):
    print my_list[i]


