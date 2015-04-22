#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


def cipher(string):

    new_s = ""

    for c in string:
        if c.islower():
            new_c = unichr(219 - ord(c))
            new_s += new_c
        else:
            new_s += c

    return new_s


if __name__ == "__main__":

    string = sys.argv[1]

    new_string = cipher(string)
    print new_string
