#! usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

for line in open(sys.argv[1], "r"):
  line = line.strip()
  sec = re.search("=(=+)([^=]*)==+", line)
  if sec:
    print sec.group(2) + ": " + str(len(sec.group(1)))
