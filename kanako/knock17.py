#!/usr/bin/python
#coding utf-8

word =[]
word_list = []
word_variety = []
for line in open("hightemp.txt"):
	word = line.strip().split()
	word_list.append(word[0])
for w in word_list:
	if w in word_variety:
		continue
	else:
		word_variety.append(w)
for words in word_variety:
	print words
