#! usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

my_dict = {}

for line in open(sys.argv[1], "r"):
  line = line.strip()

  ref = re.search("\|(.+?) = (.+?)<ref(.*)", line)
  kiso = re.search("\|(.+?) = (.*)", line)

  if ref:
    my_dict[ref.group(1)] = ref.group(2)
  elif kiso:
    my_dict[kiso.group(1)] = kiso.group(2)

for j, k in my_dict.items():
  print j + " = " + k  
