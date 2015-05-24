#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    col1s = map(lambda x: x.split("\t")[0], lines)

    for l in set(col1s):
        print l.strip()


# コマンド
# cut -f 1 hightemp.txt | sort | uniq 
