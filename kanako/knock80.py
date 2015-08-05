#!usr/bin/python
#coding:utf-8
import re

word_list = []
pattern = re.compile('^[.,!?;:()[\]\'\"]|[.,!?;:()\[\]\'\"]$')
for line in open('enwiki-20150112-400-r100-10576.txt'):
	space_spl = line.strip().split()
	for word in space_spl:
		if pattern.search(word) is not None:
			words = pattern.sub('',word)
			word_list.append(words)
		elif word == 'NULL':
			pass
f = open('enwiki.txt', 'w') 
for i in word_list:
	f.write(i+' ')
