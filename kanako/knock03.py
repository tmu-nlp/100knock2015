#!/usr/bin/python
#coding: UTF-8

def p(sentence):

	for word in sentence.split(" "):
		if "," or "." in word:
			word = word.rstrip(",")
			word = word.rstrip(".")

		print len(word),


if __name__=='__main__':
	p("Now I need a drink, alcoholic of course, after the heavy lectures i nvolving quantum mechanics.")
