#!/usr/bin/python
#coding: UTF-8
def col_1_2(my_file):
	file1 = open("col1.txt","w")
	file2 = open("col2.txt","w")
	for line in open(my_file):
		sent = line.strip().split("\t")
		file1.write(sent[0]+"\n")
		file2.write(sent[1]+"\n")
if __name__=='__main__':
	col_1_2("hightemp.txt")
