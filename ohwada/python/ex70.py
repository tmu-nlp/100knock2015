#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import random

f1 = open("rt-polaritydata/rt-polarity.neg", "r")
f2 = open("rt-polaritydata/rt-polarity.pos", "r")

lst1 = ["-1" + " " + sent for sent in f1.readlines()]
lst2 = ["+1" + " " + sent for sent in f2.readlines()]

lst = lst1 + lst2
random.shuffle(lst)

for val in lst:
    print val.strip()
