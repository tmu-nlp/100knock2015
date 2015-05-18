#!/usr/bin/python
# --*-- coding:utf-8 --*--
"""import string
in_str="Now I need a drink,alcoholic of course,after the heavy lectures involving quantum mechanics"

array = in_str.split(" ")
in_str=string.join(array,",")
#print in_str
array = in_str.split(",")
out_str=[]
for char in array:
  out_str.append(len(char))
 # print char

#print type(char)
print out_str
"""
print map(lambda x: len(x.replace(",","").replace(".","")),sentence.split(" "))


