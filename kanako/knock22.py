#!/usr/bin/python
#coding: utf-8
import re

pattern = re.compile("\[\[Category:(.*)\]\]")
for line in open("jawiki_us.txt"):
	p_search = pattern.search(line)
	if  p_search is not None:
		print p_search.group(1)
