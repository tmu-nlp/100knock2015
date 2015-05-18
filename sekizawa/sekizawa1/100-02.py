#!/usr/bin/python
#coding: utf-8↲

list1 = u"パトカー"
list2 = u"タクシー"
list3 = u""

for i in range(len(list1)):
    list3 += list1[i]
    list3 += list2[i]

print list3

