#!usr/bin/python
#--*--coding:utf-8--*--

import sys
import re

if __name__ == '__main__':
  inputfile = open(sys.argv[1],'r')
  pattern = re.compile('\[\[(File|ファイル)\:(.+?)\|.+\]\]')
  for line in inputfile:
      result = pattern.search(line)
      if result is not None:
         print result.group(2)
