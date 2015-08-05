#!/usr/bin/python
#-*-coding:utf-8-*-
#先頭からN行を出力するプログラム
#コマンドライン(param[2]はコマンドライン引数)

import sys

param = sys.argv

print param[2]
count = 1

for line in open(sys.argv[1]):
	print line.strip()
	if count == int(param[2]):
		break
	count += 1

