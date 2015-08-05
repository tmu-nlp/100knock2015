#!/usr/bin/python
#coding: UTF-8
def tab_conver(my_file):
	line = []
	for w in open(my_file):
		line.append(w.replace("\t"," "))
	f = open("tab.txt","w")
	for n in range(0,len(line)):
		f.write(line[n])
if __name__=='__main__':
	tab_conver("hightemp.txt")
