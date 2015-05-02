#!/usr/bin/python
# _*_ coding: utf-8 _*_

###駄作

import sys

n = int(sys.argv[1]) #コマンドライン引数を受け取る
yomikomi = open(sys.argv[2],"r")

line_list = []       

for line in yomikomi:
   line_list.append(line.strip())  #それぞれの行を要素にして、格納、なので長さは行数

yomikomi.close()

kakikomi = []                      #ファイルパスが各要素

for number in range(n):
    kakikomi.append(open("my_file%d.txt" % (number) , "w"))    #入力した整数個だけパス作ります

index = 0
count = 0

yomikomi = open(sys.argv[2], "r")

for line in line_list:
#    print line
#    print kakikomi[index]   
    kakikomi[index].write("%s\n" % (line))
    count += 1
    if count >= float (len(line_list)) /n:
       index +=1
       count = 0 

