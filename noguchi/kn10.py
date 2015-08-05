#! usr/bin/python
# -*- coding: utf-8 -*-
# コマンドは wc file

import sys

my_file = open(sys.argv[1], "r")
count = 0

for line in my_file:
#  line = line.strip()
  count += 1

print "行数は " + str(count) + " 行です"
