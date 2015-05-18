#!usr/bin/python
#--*--coding:utf-8--*--

import sys

if __name__ == "__main__":
  infile = open(sys.argv[1],"r")
  index = int(sys.argv[2])
  count = 0
  mylist = []
  for line in infile:
      count +=1
      mylist.append(line)
  for i in range(0,index):
      print mylist[count-index+i]  
