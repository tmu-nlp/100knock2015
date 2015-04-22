#!/usr/bin/python
#coding: UTF-8

p=[]
words = u"パタトクカシーー"

w = list(words)

for n in [0,2,4,6]:
 p += w[n]

print "".join(p)
