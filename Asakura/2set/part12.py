#!usr/bin/python
#--*--coding:utf-8--*--

import sys
if __name__ == "__main__":
  in_file = open(sys.argv[1],"r")

  f1 = open("col1.txt","w")
  f2 = open("col2.txt","w")
  for line in in_file:
      mylist = line.split("\t")
      print mylist[0]
      f1.write(mylist[0]+"\n")
      f2.write(mylist[1]+"\n")
  f1.close
  f2.close
