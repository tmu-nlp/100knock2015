#!/usr/bin/python
#-*-coding:utf-8-*-
#異なり(type)を抽出するプログラム

import sys

d = dict()#タイプしかもてない
for line in open(sys.argv[1]):
    d[line.strip()] = 0

for key in d.keys():#辞書のkeyをリストにする
    print key