#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


with open("col1.txt", "w") as f1, open("col2.txt", "w") as f2,\
     open("hightemp.txt", "r") as f3:
    for line in f3:
        line = line.strip()
        (col1, col2) = line.split("\t")[:2]
        f1.write(col1 + "\n")
        f2.write(col2 + "\n")


# コマンド
# cut -f 1 hightemp.txt
# cut -f 2 hightemp.txt
