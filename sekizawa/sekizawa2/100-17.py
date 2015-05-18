#!/usr/bin/python
#coding: utf-8

if __name__ == "__main__":

    f = open("hightemp.txt", "r")

    s = set()

    for line in f:
        words = line.split("\t")
        if words[0] not in s:
            print words[0]
            s.add(words[0])

    f.close()

