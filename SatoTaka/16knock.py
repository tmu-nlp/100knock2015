#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys

open_file  = open(sys.argv[1], "r")
n          = int(sys.argv[2])
 
o_list     = [line.strip() for line in open_file]
open_file.close

w_list = [open("w_file_%d" % (i+1), "w") for i in range(n)]

index  = 0  #w_listのインデックス
count1 = 0  #各ファイルに読み込ませる回数のためのもの　　
sho   = len(o_list)/n
amari = len(o_list)%n

mylist = []

for line in o_list: #読み込んだ行数だけループ
    w_list[index].write(line+"\n")
    count1 += 1
    if count1 == sho +1:
       mylist.append(count1)
       count1  = 0
       index  += 1
    if index == amari:
       sho   -= 1
       amari = float(amari)+0.1
print mylist
