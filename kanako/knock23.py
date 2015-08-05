#!usr/bin/python
#coding:utf-8
section = {}
count = 1
for line in open("jawiki_us.txt"):
	if line.startswith('=='):
		section[line] = count
		count +=1
for i,j in sorted(section.items(),key=lambda x:x[1]):
	print i,j
