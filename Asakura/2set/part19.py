#!usr/bin/python
#--*--coding:utf-8--*--
import sys
from collections import defaultdict
if __name__=="__main__":
  infile = open(sys.argv[1],"r")
  mylist = []
  mydict = defaultdict(lambda:0)
  for line in infile:
      mylist = line.strip().split("\t")
      mydict[mylist[0]] += 1/float(24)
  for key,value in sorted(mydict.items(),key=lambda x:x[1],reverse = True):
      print key,value
