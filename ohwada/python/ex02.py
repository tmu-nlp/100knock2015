#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


string1 = u"パトカー"
string2 = u"タクシー"

l = []
for i in range(len(string1)):
    l.append(string1[i] + string2[i])

print "".join(l)

# or
print "".join([a + b for (a, b) in zip(string1, string2)])
