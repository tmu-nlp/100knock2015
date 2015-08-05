#!usr/bin/python
#--*--coding:utf-8--*--

from part30 import *
from collections import defaultdict
def count():
  mecablist = makelist()
  countdict = defaultdict(lambda:0)
  for bunlist in mecablist:
      for mydict in bunlist:
          countdict[mydict['base']] += 1 
  return countdict
if __name__ == '__main__':
  for key,value in sorted(count().items(),key = lambda x:-x[1]):
      print key,value
