#!usr/bin/python
#--*--coding:utf-8--*--

import sys
import re

if __name__ == '__main__':
  inputfile = open(sys.argv[1],'r')
  pattern = re.compile('\[\[Category\:(((.*?)\|+.*)|(.*))\]\]')
  for line in inputfile:
      result = pattern.search(line)
      if result is not None:
         if result.group(4) is None:
            print result.group(3)
         else:
            print result.group(4)
        # print result.group(3) if result.group(4) is None else result.group(4)
