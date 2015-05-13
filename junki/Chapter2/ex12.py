#!/usr/bin/python
#-*-coding:utf-8-*-
#col1に第一コラムだけを抽出、col2に第二コラムを抽出

import sys

if __name__ == '__main__':
    col1 = open(sys.argv[2], "w")
    col2 = open(sys.argv[3], "w")
    for line in open(sys.argv[1]):
        spl = line.strip().split('\t')
        print >>col1, spl[0]
        print >>col2, spl[1]
