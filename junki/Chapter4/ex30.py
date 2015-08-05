#!/usr/bin/python
#-*-coding:utf-8-*-
#形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

import sys

mylist = []
keidict = {}
if __name__ == '__main__':
	for line in open(sys.argv[1],'r'):
		mydict = line.strip().split('\t')
		if 'EOS' in mydict:
			mydict[0] = mydict[0].replace('EOS', '')
		surface = mydict[0]
		surfacedict.append(surface)
		
		#basedict.append(mydict[1])
		#print mydict[1]
		
	for word in surfacedict:
		print word
	
	#for base in basedict.append(mydict[2]):
	#	print base