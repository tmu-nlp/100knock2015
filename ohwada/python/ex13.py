#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


with open("col1.txt", "r") as f1, open("col2.txt", "r") as f2,\
     open("col1-2.txt", "w") as f3:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    new_lines = [l1.strip() + "\t" + l2.strip() for l1, l2 in zip(lines1, lines2)]

    for line in new_lines:
        f3.write(line + "\n")


# paste col1.txt col2.txt
