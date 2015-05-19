#coding:utf-8

import sys

my_file = open(sys.argv[1], "r")

counts = 0
for line in my_file:
    counts += 1
print counts

