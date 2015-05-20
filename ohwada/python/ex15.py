#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    N = int(sys.argv[1])
    output_lines = lines[len(lines) - N:]

    for line in output_lines:
        print line.strip()


# コマンド
# tail -n N hightemp.txt
