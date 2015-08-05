#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

my_dict={}  
my_file = open(sys.argv[1], "r") #ファイルオープン
for line in my_file: #my_fileの内のline文をループをさせる
	line = line.strip() #行終端記号¥nを削除
	line = line.replace(',', '')
	line = line.replace('.', '')
	words = line.split(" ") #文を空白区切りで単語の配列に分割
	for word in words:
		if word not in my_dict: #my_doctにwordが含まれていないならmy_dict[word]を１とする
			my_dict[word]=1
		else: #それ以外ではmy_dict[word]に要素を追加していく
			my_dict[word]+=1
			
for key, bar in sorted(my_dict.items()): #各キーとその追加された要素数を表示
	print "%s %d"% (key, bar)