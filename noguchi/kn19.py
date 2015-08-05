#! usr/bin/python
# -*- coding: utf-8 -*-

import sys

my_file = open(sys.argv[1], "r")
my_dict = {}

for line in my_file:
  line = line.strip()
  words = line.split("\t")
  if words[0] in my_dict:
    my_dict[words[0]] += 1
  else:
    my_dict[words[0]] = 1

for word, num in sorted(my_dict.items(), key = lambda n: -int(n[1])):
  print word, num
