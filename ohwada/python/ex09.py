#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import random


sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."


word_list = sentence.split(" ")
new_word_list = []

for w in word_list:
    if len(w) <= 4:
        new_word_list.append(w)
    else:
        l = []
        for c in w:
            l.append(c)

        new_w = w[0]
        for i in range(len(l[1:-1])):
            rand_index = random.randint(1, len(l)-2)
            new_w += l[rand_index]
            l.pop(rand_index)
 
        new_w += w[-1]
        new_word_list.append(new_w)


print " ".join(new_word_list) 
