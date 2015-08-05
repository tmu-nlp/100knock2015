#!/usr/bin/python
#coding: utf-8
import sys
def stop_tf(word):
	stop_list = []
	for line in open("stop_word.txt"):
		stop_list.append(line.rstrip())
	return word in stop_list
if __name__=='__main__':
	word = str(sys.argv[1])
	print stop_tf(word)
