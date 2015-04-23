#!/usr/bin/python
# _*_ coding: utf-8 _*_

###わけわかめ


import sys

yomikomi = open(sys.argv[1], "r")

column_1 = []

for line in yomikomi:
    words_list = line.strip().split("\t")
    column_1.append(words_list[0])

X =  [ i for i in set(column_1) ]

for words in X:
    print words
