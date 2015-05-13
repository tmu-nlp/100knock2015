#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


string = "stressed"

l = []
for c in string:
    l.insert(0, c)

print "".join(l)

# or
print string[::-1]
