#!usr/bin/python
#coding:utf-8
import re
from knock27 import no_link

def us_info():
	base_us = {}
	pat_ref = re.compile('(<ref>.*|<ref .*)')
	pat_br = re.compile('<br.*?>')
	for i,j in no_link().items():
		base_us[i] = pat_ref.sub('',j)
		base_us[i] = pat_br.sub('',j)
	return base_us
if __name__=='__main__':
	for i,j,in sorted(us_info().items()):
		print i,j,
