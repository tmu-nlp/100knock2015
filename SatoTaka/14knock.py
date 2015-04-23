#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys

n = int(sys.argv[1]) #文字列をコマンドライン引数として読み込んでint型に変換
yomikomi = open(sys.argv[2], "r")

for line in yomikomi:
    print line
    n -= 1
    if n == 0: 
       break


