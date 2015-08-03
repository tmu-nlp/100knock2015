#!/usr/bin/python
#coding: UTF-8

def odd(words):
	p=[]
	for n in range(0,7,2):
		p += words[n]
	print "".join(p)

if __name__=='__main__':
	odd(u"パタトクカシーー")
