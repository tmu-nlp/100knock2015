#!usr/bin/python
#--*--coding:utf-8--*--

import sys

open_file = open(sys.argv[1])

print type(open_file)
count = 0
for index in open_file:
    count += 1
print count
