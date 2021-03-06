#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:
    def __init__(self,morphs,dst,srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs



def make_chunk_list():
    sentence_list = list()
    chunk_list = list()
    numbers_dict = defaultdict(list)
    for line in open(sys.argv[1],'r'):
        if line.strip() == "EOS":
            sentence_list.append(chunk_list)
            chunk_list = list()
            numbers_dict = defaultdict(list)
            continue

        elif line.startswith('*'):
            morphs = list()
            number_list = line.strip().split(" ")
            dst = number_list[2][:-1]
            chunk_list.append(Chunk(morphs,dst,numbers_dict[number_list[1]]))
            numbers_dict[dst].append(number_list[1])
            continue

        elif "\t" in line:
            surface, items = line.strip().split("\t")
            item_list = items.split(",")
            morphs.append(Morph(surface,item_list[6],item_list[0],item_list[1]))
            continue

    return sentence_list


if __name__ == '__main__':
    sentence_list = make_chunk_list()
    count = 0
    for chunk in sentence_list[1]:
        for morph in chunk.morphs:
            print morph.surface,
        print chunk.dst,chunk.srcs