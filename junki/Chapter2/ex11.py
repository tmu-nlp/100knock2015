#!/usr/bin/python
#-*-coding:utf-8-*-

#各行のタブスペースをスペースにするプログラム

import sys

text = open(sys.argv[1], "r")
for sentence in text:
	sentence = sentence.strip()
	replaceline = sentence.replace('\t',' ')
	print replaceline