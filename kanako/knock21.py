#!usr/bin/python
#coding: utf-8
import re

pattern = re.compile(r"\[\[Category")
for line in open("jawiki_us.txt"):
	if  pattern.match(line):
		print line, 
