#!usr/bin/python
#coding:utf-8

temp_list = []
high_list = []
for line in open("hightemp.txt"):
	temp_list.append(line.strip().split('\t'))
for line in sorted(temp_list,key=lambda x: -float(x[2])):
	print '\t'.join(line)
