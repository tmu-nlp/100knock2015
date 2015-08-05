#!usr/bin/python
#coding:utf-8
from knock30 import morph_read
from collections import defaultdict

def word_freq():
	word_dict = defaultdict(lambda:0)
	for sent in morph_read():
		for m_dict in sent:
			word_dict[m_dict['surface']] += 1
	return word_dict
if __name__=='__main__':
	for i,j in sorted(word_freq().items(),key = lambda x:-x[1]):
		print i,j		 
