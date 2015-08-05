#!usr/bin/python
#coding:utf-8


import sys
from stemming.porter2 import stem
def main(in_file):
    for line in open(in_file):
        print stem(line.strip()),line


if __name__ == '__main__':
    main('51result.txt')
