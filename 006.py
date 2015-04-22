#!/usr/bin/python
# --*--coding:utf-8--*--

str1 = "paraparaparadise"
str2 = "paragraph"
listX=[]
listY=[]
for index in range(len(str1)-1):
  mylist=[]
  for index2 in range(2):
    mylist.append(str1[index+index2])
  listX.append(tuple(mylist))
index = 0
index2 = 0
for index in range(len(str2)-1):
  mylist=[]
  for index2 in range(2):
    mylist.append(str2[index+index2])
  listY.append(tuple(mylist))
print listX
print listY

list1 = set(listX)
list2 = set(listY)

salist = list1 - list2
walist = list1 | list2
sekilist = list1 & list2
holist = list1 ^ list2
print "和集合:"  ,walist
print "差集合:"  ,salist
print "積集合:"  ,sekilist
if ('s','e') in listX:
  print "listXに含まれる"
elif ('s','e') in listY:
  print "listYに含まれる"
else:
  print "含まれない"
