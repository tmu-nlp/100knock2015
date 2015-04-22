#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

d = {}
word_list = sentence.split(" ")

l = []
for w in word_list:
    if w[-1] in [",", "."]:
        w = w[:-1]
    l.append(len(w))

print l    

