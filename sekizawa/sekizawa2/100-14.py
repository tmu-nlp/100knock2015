#!/usr/bin/python
#coding: utf-8

import sys

if __name__ == "__main__":

    f = open("hightemp.txt", "r")

    N = sys.argv
    count = 0

    while count < int(N[1]):
        for line in f:
            print line
            count += 1
            break

f.close()

