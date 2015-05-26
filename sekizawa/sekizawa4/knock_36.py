#!usr/bin/python
#coding:utf-8

from collections import defaultdict

def freq():

    f = open("neko.txt.mecab", "r")
    freq = defaultdict(lambda: 0)

    for line in f:
        line = line.strip().replace(" ", "")
        line = unicode(line, "utf-8")
        words = line.split(",")
        word = words[0].encode("utf-8")

        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

    return freq

if __name__ == "__main__":
    dic = freq()
    for key, value in sorted(dic.items(), key = lambda x:x[1], reverse = True):
        print "%s %d" % (key, value)

