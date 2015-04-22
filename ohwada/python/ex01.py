#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


string = u"パタトクカシーー"

l = []
for i in [1,3,5,7]:
    l.append(string[i-1])

print "".join(l)

# or
print "".join(string[0:7:2])
