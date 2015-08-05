#!/usr/bin/python
#coding: UTF-8
import re

def sent_div():
	sent_list = []
	doc_list = []
	pattern_list = []
	pattern = re.compile("(.+[.:;?!])\s([A-Z].+)")
	pattern_g0 = re.compile(".+[.:;?!]")
	for line in open("nlp.txt"):
		pattern_list = pattern.findall(line)
		if pattern.search(line) is not None:
			for i in pattern_list:
				for j in i:
					pattern_sent = pattern_g0.match(j)
					sent_list.append(pattern_sent.group(0))
					doc_list.append(sent_list)
					sent_list = []
			pattern_list = []
		else:
			sent_list.append(line.rstrip())
	return doc_list
	
if __name__=='__main__':
	for i in sent_div():
		print ''.join(i)
	
