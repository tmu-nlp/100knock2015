#!/usr/bin/python
#coding: UTF-8
def ele(sentence):
	dic = {}
	x = [1,5,6,7,8,9,15,16,19]
	for n , word in enumerate(sentence.split(" ")):
		if n + 1 in x:
			dic[word[0]] = n + 1
		else:
			dic[word[0:2]] = n + 1
	print sorted(dic.items(),key = lambda dic:dic[1])

if __name__=='__main__':
	ele("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")                  
