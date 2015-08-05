#!/usr/bin/python
#-*-coding:utf-8-*-
#末尾からN行を出力するプログラム
#コマンドライン(param[2]はコマンドライン引数)

import sys

param = sys.argv

print param[2]
count = 1
line = open(sys.argv[1])
reverseslice = line[::-1]
for lines in reverseslice:
	print lines
	
for line in reverseslice:
	print line.strip()
	if count == int(param[2]):
		break
	count += 1