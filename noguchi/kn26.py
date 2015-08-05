#! usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

my_dict = {}
kiso = re.compile("\|(.+?) = (.*)")
ref = re.compile("(.+?)<ref[ |>].*")
kyou = re.compile("(.+?)'+(.+?)'+(.*)")

for line in open(sys.argv[1], "r"):
  line = line.strip()
  kiso_match = kiso.search(line)
  if kiso_match:
    ref_match = ref.search(kiso_match.group(2))
    kyou_match = kyou.search(kiso_match.group(2))
    if ref_match:
      my_dict[kiso_match.group(1)] = ref_match.group(1)
    elif kyou_match:
      my_dict[kiso_match.group(1)] = kyou_match.group(1) + kyou_match.group(2) + kyou_match.group(3)
    else:
      my_dict[kiso_match.group(1)] = kiso_match.group(2)

for j, k in my_dict.items():
  print j + " = " + k
