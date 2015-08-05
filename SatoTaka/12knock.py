#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys

yomikomi = open(sys.argv[1], "r")
kakikomi_1 = open("col1.txt", "w")
kakikomi_2 = open("col2.txt", "w")

first = []
second = []

for line in yomikomi:
    words = line.split("\t")
    first=words[0]
    second=words[1]

    kakikomi_1.write("%s\n" %first)	
    kakikomi_2.write("%s\n" %second)

kakikomi_1.close()    
kakikomi_2.close()    
