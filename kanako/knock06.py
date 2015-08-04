#!/usr/bin/python
#coding: UTF-8

def syugo(sent1,sent2,n):
	X = set(mozi_ngram(sent1,n))
	Y = set(mozi_ngram(sent2,n))
	print "和集合：",(X | Y)
	print "積集合：",(X & Y)
	print "差集合：",(X ^ Y)
	if "se" in X:
		print "'se'という%d-gramが%sに含まれます"%(n,sent1)
	else:
		print "'se'という%d-gramは%sに含まれません"%(n,sent1)
	if "se" in Y:
		print "'se'という%d-gramが%sに含まれます"%(n,sent2)
	else:
		print "'se'という%d-gramは%sに含まれません"%(n,sent2)

def mozi_ngram(sentence,n):
	ngram = []
	ngram_list =[]
	sent = list(sentence)
	for num in range(len(sent)-n+1):
		for num2 in range(n):
			ngram.append(sent[num+num2])
		ngram_list.append("".join(ngram))
		ngram = []
	return ngram_list

if __name__=='__main__':
	syugo("paraparaparadise","paragraph",2)
