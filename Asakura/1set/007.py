#!/usr/bin/python
# --*--coding:utf-8--*--

import sys

mylist = sys.argv[1::]

def kansuu(x,y,z):
  mystr = x + "時の" + y + "は" + z
  return mystr

print kansuu(mylist[0],mylist[1],mylist[2])
