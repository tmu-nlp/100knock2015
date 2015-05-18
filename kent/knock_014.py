#coding:utf-8

import sys

my_file = open("hightemp.txt", "r")
num = sys.argv
n = int(num[1])

for line in my_file:
    print line.strip()
    n -= 1
    if n == 0:
       break

"""
words = []
for line in my_file:
    words.append(line.strip())
for index in range(int(n)):
    print words[index]
"""    
