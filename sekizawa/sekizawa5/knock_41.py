#!usr/bin/python
#coding:utf-8

import re
import knock_40
from collections import defaultdict

class Morph(object):
    def __init__(self, line):
        feature = line.replace("\t", ",").split(",")
        self.surface = unicode(feature[0], "utf-8")
        self.base    = unicode(feature[8], "utf-8")
        self.pos     = unicode(feature[1], "utf-8")
        self.pos1    = unicode(feature[2], "utf-8")


class Chunk(object):
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs


def main(number):
    sentence_dict = knock_40.Sentence_List("neko.txt.cabocha")
    morphs = []
    srcs = []
    chunk_list = []
    dst_list = []
    srcs_dict = defaultdict(list)
    flag = 0

    for line in sentence_dict[number]:
        if re.match("\*", line):
            if flag == 1:
                chunking = Chunk(morphs, dst, srcs_dict[features[1]])
                morphs = []
                srcs = []
                dst_list.append(dst)
                chunk_list.append(chunking)
            flag = 1
            features = line.strip().split(" ")
            dst = features[2].replace("D", "")
            srcs_dict[dst].append(features[1])

        elif "\t" in line:
            morphing = Morph(line)
            morphs.append(morphing)
        else:
            chunking = Chunk(morphs, dst, srcs_dict[features[1]])
            chunk_list.append(chunking)
            break
    return chunk_list


if __name__ == "__main__":
    chunk_list = main(5)

    for chunks in chunk_list:
        for morph in chunks.morphs:
            print morph.surface,
        print chunks.dst, chunks.srcs


