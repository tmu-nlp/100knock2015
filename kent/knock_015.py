#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

num = sys.argv
n = int(num[1])
count = 0
print n
my_file = open("hightemp.txt", "r")

line1 = []
for line in my_file:
    line1.append(line.strip().decode("utf-8"))
    if count >= n:
        line1.pop(0)
    count += 1

for i in line1:
    print i


"""
    n1 += 1
    if n1 == 24:
        break
"""
