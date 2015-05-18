#! usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

my_file = open(sys.argv[1], "r")

for line in my_file:
  line = line.strip()
  if re.search("\[\[Category:.*\]\]", line):
    print line
