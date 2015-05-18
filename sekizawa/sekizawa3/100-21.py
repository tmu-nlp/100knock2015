#!/usr/bin/python
#coding: utf-8

import re

if __name__ == "__main__":

    f = open("UK.json", "r")

    pattern = re.compile("Category")
    for line in f:
        judge = pattern.search(line)
        if judge:
            print line,

    f.close()


