#!/usr/bin/python
#_*_ coding: utf-8 _*_

import sys

yomikomi = open(sys.argv[1], "r")
n        = int(sys.argv[2])
k_list   = [open("write_file%d" % (i+1), "w") for i in range(n)]
y_list   = [line.strip() for line in yomikomi]
length   = len(y_list)  #行数
sho      = length/n     #各ファイルに書き込む行数
amari    = length%n     #行数の多いファイル数
count    = index_k = index_y = 0 

for index_k in range(n):
    if index_k == n-amari:
       sho   += 1
       amari += 0.1
    for index_y in range(count, count+sho):
        k_list[index_k].write("%s\n" % (y_list[index_y]))
    count += sho
