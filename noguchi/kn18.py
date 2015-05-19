#! usr/bin/python
# -*- coding: utf-8 -*-

import sys

my_file = open(sys.argv[1], "r")
line_list = []

for line in my_file:
  line = line.strip()
  words = line.split("\t")
  line_list.append(words)

sorted_list = sorted(line_list, key = lambda words: -float(words[2]))

for word in sorted_list:
  print "\t".join(word)
