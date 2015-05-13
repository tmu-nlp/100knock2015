#! usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

for line in open(sys.argv[1]):
  f = re.search("\[\[(File|ファイル):(.+?)\|.*\]\]", line)
  if f:
    print f.group(2)
