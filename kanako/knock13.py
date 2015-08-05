#!/usr/bi/python
#coding: utf-8

col_file = open("col.txt","w")
for i,j in zip(open("col1.txt"),open("col2.txt")):
	col_file.write(i.strip() + "\t" + j)
