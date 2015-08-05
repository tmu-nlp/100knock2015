#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
my_file = open(sys.argv[1], "r")

for line in my_file:
	line = line.replace(',', '')
	line = line.replace('.', '')
	words = line.split(" ")

for i, word in enumerate(words):#words(スペース)で区切られたリストの添え字を抽出する
    head = [1, 5, 6, 7, 8, 9, 15, 16, 19]#headとしてlistを設定
    if i+1 in head:#headの添え字の時最初の一文字目を表示
        print "%s %d" % (word[0:1], i+1)
    else:
        print "%s %d" % (word[0:2], i+1)