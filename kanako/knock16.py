#!/usr/bin/python
#coding: UTF-8
import sys
def n_split(my_file):
	num = int(sys.argv[1])
	line = open(my_file).readlines()
	line_div = len(line)/num
	line_rem = len(line)%num
	for n in range(line_rem):
		for m in range(line_div+1):
			print line[n*(line_div+1)+m],
		print
	for n in range(num-line_rem):
		for m in range(line_div):
			print line[((line_div+1)*line_rem+m)+n*line_div],
		print
if __name__=='__main__':
	n_split("hightemp.txt")
