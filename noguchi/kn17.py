#! usr/bin/python
# -*- coding: utf-8 -*-

import sys

my_file = open(sys.argv[1], "r")
set1 = set()

for line in my_file:
  line = line.strip()
  word = line.split("\t")
  set1.add(word[0])

for word in set1:
  print word
