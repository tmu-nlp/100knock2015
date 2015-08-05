#!usr/bin/python
#coding:utf-8
import re

def base_info():
	bace_dict = {}
	field = re.compile("\|(.+?)\s\=\s(.+?)")
	spl = re.compile("(.+?)\s\=\s")
	for line in open("jawiki_us.txt",'r'):
		pattern = field.search(line)
		spl_pattern = spl.split(line)
		if pattern is not None:
			bace_dict[pattern.group(1)] = spl_pattern[2] 
	for i,j in bace_dict.items():
		print i,j,
if __name__=='__main__':
	base_info()
