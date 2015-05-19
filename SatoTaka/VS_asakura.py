#!/usr/bin/python
# _*_ coding:utf-8 _*_
import sys
n = int(sys.argv[1])
list1 = [24/n +1 if i<24%n else 24/n for i in range(n)]
lines = [line.strip() for line in open(sys.argv[2], "r")]
index = 0
for i in range(n):
    write_file = open("w_f_%d.txt" % (i) , "w")
    for kaisu in range(list1[i]):
        write_file.write(lines[index]+"\n")
        index+=1

"""
list1 = [24/n if n-24%n>i else 24/n +1 for i in range(n)]
print list1
"""


"""
list1 = []
sho   = 24/n
ama   = 24%n
for i in range(n):
    list1.append(sho)
    if n-24%n == i+1:
       sho += 1
print list1
"""



"""
sho   = 24/n
ama   = 24%n
list1 = []
for i in range(n):
    list1.append(sho)
    amari += 1
    if n-amari == 0:
       amari += 0.1
       sho   += 1
print list1
"""
