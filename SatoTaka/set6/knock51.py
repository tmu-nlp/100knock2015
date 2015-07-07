#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys

def main():
    input_file = open(sys.argv[1], "r")
    for line in input_file:
        words = line.strip().split(" ")
        for word in words:
            print word
    input_file.close()

if __name__=="__main__":
   main()
