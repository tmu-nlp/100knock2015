#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


with open("hightemp.txt", "r") as f:
    lines = f.readlines()

    split_lines = [line.split("\t") for line in lines]
    sorted_lines = sorted(split_lines, key=lambda x: x[2], reverse=True)

    for line in reversed(sorted_lines):
        print "\t".join(line).strip()



# コマンド
# sort -k 3 hightemp.txt 
