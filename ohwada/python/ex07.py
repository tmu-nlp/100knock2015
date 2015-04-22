#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


def func(x, y, z):
    
    return x + "時の" + y + "は" + z


if __name__ == "__main__":
    (x, y, z) = sys.argv[1:4]

    string = func(x, y, z)
    print string
    

