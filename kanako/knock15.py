#!/usr/bin/python
#coding: UTF-8
import sys
def end_line(my_file):
	num = int(sys.argv[1])
	line = open(my_file).readlines()
	line.reverse()
	for n in range(0,num):
		print line[n],
if __name__=='__main__':
	end_line("hightemp.txt")
