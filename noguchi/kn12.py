#! usr/bin/python
# -*- coding: utf-8 -*-
# コマンドは cut -f N file

import sys

my_file1 = open(sys.argv[1], "r")
my_file2 = open("col1.txt", "w")
my_file3 = open("col2.txt", "w")
co1 = []
co2 = []

for line in my_file1:
  line = line.strip()
  words = line.split("\t")
  co1.append(words[0])
  co2.append(words[1])

my_file2.write("\n".join(co1))
my_file3.write("\n".join(co2))
my_file2.close()
my_file3.close()
