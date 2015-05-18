#! usr/bin/python
# -*- coding: utf-8 -*-

import sys

my_file = open(sys.argv[1], "r")
num = int(sys.argv[2])
words = []

for line in my_file:
  line = line.strip()
  words.append(line)

if len(words) > num:
  block = len(words) / num
  surp = len(words) % num
  n = 0
  for i in range(num):
    print "\n".join(words[n:n + block])
    n += block
    if surp > 0:
      print words[n]
      n += 1
      surp -= 1
    print ""
else:
  print "行数より多くは分割しません"
