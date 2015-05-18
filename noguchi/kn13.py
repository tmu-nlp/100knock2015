#! usr/bin/python
# -*- coding: utf-8 -*-
# コマンドは paste file1 file2

import sys

my_file1 = open("col1.txt", "r")
words1 = []
my_file2 = open("col2.txt", "r")
words2 = []

for line in my_file1:
  line = line.strip()
  words1.append(line)

for line in my_file2:
  line = line.strip()
  words2.append(line)

for i in range(len(words1)):
  print words1[i] + "\t" + words2[i]
