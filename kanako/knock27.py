#!usr/bin/python
#coding:utf-8
import re
from knock26 import base_info

def no_link():
	base_no_link = {}
	link_p = re.compile('(\[\[)|(\]\])')
	for i,j in base_info().items():
		base_no_link[i] = link_p.sub('',j)
	return base_no_link
if __name__=='__main__':
	for i,j,in no_link().items():
		print i,j,
