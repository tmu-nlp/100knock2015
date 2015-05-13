#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys

yomikomi = open(sys.argv[1], "r")

my_list = []

for line in yomikomi:
    if "\t" in line:
       line.replace("\t", " ")
    my_list.append(line)

for sentence in my_list:
    print sentence
