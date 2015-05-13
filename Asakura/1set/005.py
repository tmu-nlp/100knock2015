#!/usr/bin/python
#--*--coding:utf-8--*--
import sys

mystr="I am an NLPer"

array=mystr.split(" ")
argv = sys.argv 
n=int(argv[1])
count = 0
mylist2=[]
mylist3=[]
print "n:%d"%n
for index in range(len(array)-n+1):
  mylist=[]
  for index2 in range(n):
    mylist.append(array[index+index2])
  mylist2.append(tuple(mylist))
print mylist2
moziretu="".join(array)#string.join(array,"") 
for index3 in range(len(moziretu)-n+1):
  mylist=[]
  for index4 in range(n):
    mylist.append(moziretu[index3+index4])
  mylist3.append(tuple(mylist))
print mylist3

  
