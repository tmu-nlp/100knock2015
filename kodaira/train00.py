#!/usr/bin/python

from collections import defaultdict
import sys

#load file
my_file = open(sys.argv[1], "r")

my_dict = defaultdict(lambda: 1)


for line in my_file:
  sentence = line.strip()
  words = sentence.split(" ")
  for word in words:
    if word in my_dict:
      my_dict[word] += 1
    else:
      my_dict[word]

for foo, bar in sorted (my_dict.items() ):
  print "%s --> %r" % (foo, bar)

