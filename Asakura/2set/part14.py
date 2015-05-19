#!usr/bin/python
#--*--coding:utf-8--*--

import sys
if __name__ =="__main__":
  infile = open(sys.argv[1],"r")
  imput =int(sys.argv[2])
  for line,index in zip(infile,range(0,imput)):
      print line,
