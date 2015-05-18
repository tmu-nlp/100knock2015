#!/usr/bin/python
#coding: utf-8

import re

if __name__ == "__main__":

    f = open("UK.json", "r")

    pattern = re.compile("(\=\=+)(.*?)(\=\=+)")
    for line in f:
        judge = pattern.search(line)
        if judge:
            print "%s   %d" % (judge.group(2), len(judge.group(1)) - 1)

    f.close()

