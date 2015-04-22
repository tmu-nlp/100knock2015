#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


def func(x, y, z):
   
     return "{0}時の{1}は{2}".format(x, y, z)
    

if __name__ == "__main__":
    (x, y, z) = sys.argv[1:4]

    string = func(x, y, z)
    print string
    

