#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    N = int(sys.argv[1])

    x1 = -(-len(lines) / N)
    x2 = len(lines) / N
    r = len(lines)
    c = 0
    while True:
        if r % x1 == 0 and x1 * (N - c) + x2 * c == len(lines):
            linage_lst = [x1] * (N - c) + [x2] * c
            break
        r -= x2
        c += 1

    print linage_lst

    i = 1
    for linage in linage_lst:
        with open("result_ex16/f{0}.txt".format(str(i).zfill(2)), "w") as f_sub:
            sub_lines = lines[:linage]
            text = "".join(sub_lines)
            f_sub.write(text)
        lines = lines[linage:]
        i += 1

        
