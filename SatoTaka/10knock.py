#!/usr/bin/python 
# _*_ coding: utf-8 _*_

import sys

yomikomi = open(sys.argv[1], "r")

count = 0

for line in yomikomi:
    count += 1

print count


