#!/usr/bin/python
#coding: UTF-8

def alt(words1,words2): 
	p = list()
	w1 = list(words1)
	w2 = list(words2)

	for n,m in zip(w1,w2):   
		p += n
		p += m
   
	print "".join(p)

if __name__=='__main__':
	alt(u"パトカー",u"タクシー")
