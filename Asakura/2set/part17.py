#!usr/bin/python
#--*--coding:utf-8--*--
import sys
if __name__ == "__main__":
  infile = open(sys.argv[1],"r")
  mylist =set()
  for line in infile:
     array = line.strip().split("\t")
     mylist.add(array[0])
  for i in mylist:
      print str(i) 
