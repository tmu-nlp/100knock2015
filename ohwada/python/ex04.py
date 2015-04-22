#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

word_list = string.split(" ")
d = {}

i = 1
for w in word_list:
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        d[w[0]] = i
    else:
        d[w[:2]] = i
    i += 1

for c, i in d.items():
    print c, i

