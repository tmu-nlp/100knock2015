#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    N = int(sys.argv[1])
    output_lines = lines[:N]

    for line in output_lines:
        print line.strip()


# コマンド
# head -n N hightemp.txt



