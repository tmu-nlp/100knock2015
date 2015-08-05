#!/usr/bin/python
#coding: UTF-8
from knock50 import sent_div

def word_del():
	word = []
	sent = []
	for i in sent_div():
		for j in i:
			if j == '':
				del(j)
			else:
				word.append(j.strip().split(" "))
	return word
if __name__=='__main__':
	for i in word_del():
		for j in i:
			print j
		print
