#!/usr/bin/python
#coding: UTF-8

def tango_ngram(sentence,n):
	dic = []
	for c,tango in enumerate(sentence.split(" ")):
		dic.append(tango)
	for num in range(c-n+2):
		print num+1,":",
		for num2 in range(n):
			print dic[num+num2],
	print
def mozi_ngram(sentence,n):
	sent = list(sentence)
	for c,i in enumerate(sent):
		if i == " " :
			del sent[c]
	for num in range(c-n+2):
		print num+1,":",
		for num2 in range(n):
			print sent[num+num2],

if __name__=='__main__':
	tango_ngram("I am an NLPer",2)
	mozi_ngram("I am an NLPer",2)
