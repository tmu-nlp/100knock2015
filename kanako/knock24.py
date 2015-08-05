#!usr/bin/python
#coding:utf-8
import re

def media_file(us_file):
	pattern = re.compile("\[\[File\:(.+?)\|.+")
	for line in open(us_file,'r'):
		file_exist = pattern.match(line)
		if file_exist is not None:
			print file_exist.group(1)
if __name__=='__main__':
	media_file("jawiki_us.txt")
