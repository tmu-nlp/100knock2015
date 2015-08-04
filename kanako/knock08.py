#!/usr/bin/python
#coding: UTF-8
import re
def cipher(sent):
	word = ""
	for w in sent:
		pattern = re.compile("[a-z]")
		if pattern.match(w):
			word += chr(219 - ord(w))
		else:
			word += w
	return word


if __name__=='__main__':
	print "暗号化：",cipher("I am an NLPer")
	print "複合化：",cipher("I zn zm NLPvi")
