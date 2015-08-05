#!usr/bin/python
#coding:utf-8
import re

def base_info():
	base_dict = {}; base_no_empha = {}
	field = re.compile("\|(.+?)\s\=\s(.+?)")
	spl = re.compile("(.+?)\s\=\s")
	empha = re.compile("\'\'+")
	for line in open("jawiki_us.txt",'r'):
		pattern = field.search(line)
		spl_pattern = spl.split(line)
		if pattern is not None:
			base_dict[pattern.group(1)] = spl_pattern[2]
	for i,j in base_dict.items():
		base_no_empha[i] = empha.sub('',j)
	return base_no_empha 
if __name__=='__main__':
	for i,j in sorted(base_info().items()):
		print i,j,
