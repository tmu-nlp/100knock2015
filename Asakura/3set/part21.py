#!usr/bin/python
#--*--coding:utf-8--*--

import sys
import re

if __name__ == '__main__':
  category = re.compile('\[\[Category\:.*\]\]')
  for line in open(sys.argv[1]):
    if category.match(line) is not None:#match
          print line.strip()
