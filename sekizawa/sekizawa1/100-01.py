#!/usr/bin/python
#coding: utf-8

list1 = u"パタトクカシーー"

list2 = u""

for i in range(len(list1) // 2):
    list2 += (list1[2 * i])

print list2

