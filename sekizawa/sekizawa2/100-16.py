#!/usr/bin/python
#coding: utf-8

import sys

if __name__ == "__main__":

    f1 = open("hightemp.txt", "r")

    N = sys.argv
    total = 0
    count = 0

    for line in f1:
        total += 1

    f1.close()
    f2 = open("hightemp.txt", "r")

    for line in f2:
        print line
        count += 1
        if count > total/int(N[1]):
            count = 0
            print "-----------------------------------------"

    f1.close()
    f2.close()
     
