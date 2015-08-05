#!/usr/bin/python
#coding: utf-8
 
word =[]
word_list = []
word_var = {}
for line in open("hightemp.txt"):
	word = line.strip().split()
	if word[0] in word_var.keys():
		word_var[word[0]] +=1
	else:
		word_var[word[0]] = 1
for i,j in sorted(word_var.items(),key=lambda x:x[1],reverse=True):
	print i,j
