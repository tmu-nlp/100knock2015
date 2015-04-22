#!/usr/bin/python
#coding: UTF-8

words1 = u"パトカー"
words2 = u"タクシー"

p =""
index = 0

w1 = list(words1)
w2 = list(words2)

for n in w1:
   p += n
   p += w2[index]
   index += 1


print "".join(p)
