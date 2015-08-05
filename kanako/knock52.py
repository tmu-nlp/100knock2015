#!usr/bin/python
#coding:utf-8
from stemming.porter2 import stem
from knock51 import word_del

def word_stem():
	word_tab_stem = {}
	for sent in word_del():
		for word in sent:
			word_tab_stem[word] = stem(word)
	return word_tab_stem
if __name__=='__main__':
	for i,j in word_stem().items():
		print i,'\t',j

