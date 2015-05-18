#!/usr/bin/python
#coding: utf-8

import sys
from collections import defaultdict

if __name__ == "__main__":

    my_dict = defaultdict(lambda: 0)

    f = open("hightemp.txt", "r")
    i = 0
    char = []

    for line in f:
        line = line.strip()
        char.append(line)
        words = line.split("\t")
        if words[2] not in my_dict:
            my_dict[words[2] + str(i)] = i
        i += 1

    for a, b in sorted(my_dict.items()):
        print char[b]

    f.close()

