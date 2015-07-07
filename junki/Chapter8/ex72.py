#!/usr/bin/python
# coding:utf-8

import sys
from stemming.porter2 import stem

def main(in_fname):
    for line in open(in_fname):
        print stem(line.strip())
        
if __name__ == '__main__':
    main(sys.argv[1])

 