#!/usr/bin/python
#-*-coding:utf-8-*-
#出現頻度を調べ、頻度順にソートするプログラム

import sys
from collections import defaultdict

d = defaultdict(lambda:int())
for line in open(sys.argv[1]):
    d[line.strip().split()[0]] += 1

for key, value in sorted(d.items(), key=lambda x: -x[1]):
    print value, key
