#! usr/bin/python
# -*- coding: utf-8  -*-
# コマンドは sed "s/¥t/ /g" file?

import sys

my_file = open(sys.argv[1], "r")

for line in my_file:
  line = line.strip()
  line = line.replace("\t", " ")
  print line
