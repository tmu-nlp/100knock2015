#!/usr/bin/python
#coding: utf-8

from collections import defaultdict

if __name__ == "__main__":

    my_dict = defaultdict(lambda: 0)

    f = open("hightemp.txt", "r")

    for line in f:
        words = line.split("\t")
        if words[0] not in my_dict:
            my_dict[words[0]]  = 1
        else:
            my_dict[words[0]] += 1

    for a,b in sorted(my_dict.items(), key = lambda x:x[1], reverse = True):
        print "%s  %d" % (a, b)

f.close()

