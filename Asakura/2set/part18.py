#!usr/bin/python
#--*--coding:utf-8--*--
import sys
from operator import itemgetter
if __name__ == "__main__":
  infile = open(sys.argv[1],"r")
  mylist1=[]
  count = 0
  for line in infile:
      mylist1.append(line.strip().split("\t"))
  mylist2 = sorted(mylist1,key=itemgetter(2))
  
  for i in mylist2:
     print  "\t".join(i)
