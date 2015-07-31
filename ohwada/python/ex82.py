#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import random


def extr_context(f, f_out):
    count = 0
    for line in f:
        words = line.strip().split(" ")
        i = 0
        for word in words:
            d = random.randint(1,5)
            if i-d < 0:
                context = words[0:i] + words[i+1:i+d+1]
            else:
                context = words[i-d:i] + words[i+1:i+d+1]
            i += 1
            
            for c in context:
                f_out.write(word + "\t" + c + "\n")



if __name__ == "__main__":
    f = open("corpus.txt", "r")
    f_out = open("context.txt", "w")
    extr_context(f, f_out)
