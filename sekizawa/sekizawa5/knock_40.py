#!usr/bin/python
#coding:utf-8

import re
from collections import defaultdict


class Morph(object):
    def __init__(self, line):
        feature = line.replace("\t", ",").split(",")
        self.surface = unicode(feature[0], "utf-8")
        if len(feature) > 8:
            self.base = unicode(feature[8], "utf-8")
        else:
            self.base = unicode("*", "utf-8")
        self.pos     = unicode(feature[1], "utf-8")
        self.pos1    = unicode(feature[2], "utf-8")

def Sentence_List(file_name):
    input_file = open(file_name, "r")
    sentence_dict = defaultdict(list)
    count = 0

    for line in input_file:
        line = line.strip()
        if line != "EOS":
            sentence_dict[count].append(line)
        else:
            sentence_dict[count].append(line)
            count += 1
    return sentence_dict


if __name__ == "__main__":
    sentence_dict = Sentence_List("neko.txt.cabocha")
    morph_list = []

    for line in sentence_dict[3]:
        print line
        if re.match("\*", line) < 1 and line != "EOS":
            classing = Morph(line)
            morph_list.append(classing)

    for morphs in morph_list:
        print "surface: " + morphs.surface,
        print "base:    " + morphs.base,
        print "pos:     " + morphs.pos,
        print "pos1:    " + morphs.pos1


