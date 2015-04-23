#!/usr/bin/python
# _*_ coding: utf-8 _*_

###駄作

import sys

n = int(sys.argv[1]) #コマンドライン引数を受け取る
yomikomi = open(sys.argv[2],"r")

words = []

for line in yomikomi:
    words.append(line)

kakikomi = []

for number in range(len(words)/n):
    kakikomi.append(open("my_file%d.txt" % (number) , "w"))

index = 0

for line in yomikomi:
    count = 0   
    kakikomi[index].write(line)
    count += 1
    if count == n:
       index +=1





