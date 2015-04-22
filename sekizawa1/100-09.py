#!/usr/bin/python
#coding: utf-8
import random

sentence  = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind"

words = sentence.split(" ")

i = -1
for word in words:
    i += 1
    if len(word) > 4:
        top = str(word[0])
        end = str(word[len(word) - 1])
        word = word.lstrip(str(top))
        word = word.rstrip(str(end))
        make = ""
        while len(word) > 0:
            char = random.choice(word)
            word = word.replace(str(char), "", 1)
            make = make + char
        word = top + make + end
        words[i] = word

print words


