#!/usr/bin/python
# --*-- coding:utf-8 --*--
from string import join
str1 = u"パトカー"
str2 = u"タクシー"
my_list=[]
for x,y in zip(str1,str2):
  print x,
  print y,
  my_list.append(x)
  my_list.append(y)
  output = join(my_list,"")
