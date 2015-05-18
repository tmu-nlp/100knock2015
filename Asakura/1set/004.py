#!/usr/bin/python
#--*--coding:utf-8--*--

in_str="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

mylist=[]
mylist=in_str.split(" ")
mydict={}
count = 0
for string in mylist:
  count+=1
  if count == [1,5,6,7,8,9,15,16,19]:
    mydict[string[0:1]]=count
  else:
    mydict[string[0:2]]=count


print mydict








