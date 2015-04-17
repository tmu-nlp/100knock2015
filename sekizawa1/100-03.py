#!/usr/bin/python

line = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = line.split(" ")

for word in words:
    count = 0
    for i in range(len(word)):
        if 'a' <= word[i] <= 'z' or 'A' <= word[i] <= 'Z':
            count += 1
    print count,

