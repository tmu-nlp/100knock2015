#!/usr/bin/python
# _*_ coding:utf-8 _*_

from stemming.porter2 import stem
import sys

def main():
    nlp_file = open(sys.argv[1], "r")
    for line in nlp_file:
        words = line.strip().split(" ")
        for word in words:
            print stem(word)

    nlp_file.close()

if __name__=="__main__":
   main()
