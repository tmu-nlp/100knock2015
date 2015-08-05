#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from collections import defaultdict


def cul_average(lines):
    dic = defaultdict(float)
    for line in lines:
        line = line.strip()
        (score_name, score) = line.split(" ")
        dic[score_name] += float(score)

    for score_name, score in dic.items():
        print score_name, score / 5


if __name__ == "__main__":
    lines = sys.stdin
    cul_average(lines)
