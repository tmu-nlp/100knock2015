#!usr/bin/python
#coding:utf-8

import MeCab
import sys

if __name__ == "__main__":

    f = open("neko.txt", "r")
    new = open("neko.txt.mecab", "w")
    tag = MeCab.Tagger (" ".join(sys.argv))

    for line in f:
        node = tag.parseToNode(line.strip())
        while node:
            print "%s %s" % (node.surface, node.feature)
            new.write(node.surface)
            new.write(",")
            new.write(node.feature)
            new.write("\n")
            node = node.next

    f.close()
    new.close()


