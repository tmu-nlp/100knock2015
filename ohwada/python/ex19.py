#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from collections import defaultdict


with open("hightemp.txt", "r") as f:
    lines = f.readlines()

    freq_dict = defaultdict(int)
    for line in lines:
        col1 = line.split("\t")[0]
        freq_dict[col1] += 1

    for s, f in sorted(sorted(freq_dict.items(), reverse=True), key=lambda x: x[1], reverse=True):
        print s



# コマンド
# cut -f 1 hightemp.txt | sort | uniq -c| sort -k 1 -r 
