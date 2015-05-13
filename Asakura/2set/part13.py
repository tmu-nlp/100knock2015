#!usr/bin/python
#--*--coding:utf-8--*--
import sys
if __name__ =="__main__":
  infile1 = open(sys.argv[1],"r")
  infile2 = open(sys.argv[2],"r")
  mylist = []
  f=open("merge","w")
  mylist= [line1.strip()+"\t"+line2.strip() for line1,line2 in zip(infile1,infile2)]
  for i in mylist:
      print i
      f.write(i+"\n")
