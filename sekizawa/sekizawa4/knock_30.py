#!usr/bin/python
#coding:utf-8

from collections import defaultdict

def analyze():
    f = open("neko.txt.mecab", "r")
    sentlist = []

    for line in f:
        dic = defaultdict(lambda: 0)
        line = line.strip().replace(" ", "")
        line = unicode(line, "utf-8")
        words = line.split(",")

        if words[1] != "BOS/EOS":
            dic["surface"] = words[0]
            if len(words) > 9:
                dic["base"]    = words[8]
            else:
                dic["base"]    = "*"
            dic["pos"]     = words[1]
            dic["pos1"]    = words[2]
            sentlist.append(dic)

    return sentlist

    f.close()

def main():
    mecablist = analyze()
    for line in mecablist:
        for key, value in line.items():
            print key,
            print value,
        print "\n"

if __name__ == "__main__":
    main()


