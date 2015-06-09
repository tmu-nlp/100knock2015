# coding: utf-8

import sys
from collections import defaultdict


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs


def make_chunk_class(fin):
    one_sent_list = list()
    all_sent_list = list()
    morphs = list()
    index_dst_list = list()
    return_chunk_flag = False

    for line in fin:
        line = line.strip()
        if line != "EOS":
            if "* " in line:
                if return_chunk_flag:
                    dst = str(dst)
                    one_sent_list.append(Chunk(morphs, dst, srcs))
                    morphs = list()
                else:
                    return_chunk_flag = True
                chunk = line.split(" ")
                index = int(chunk[1])
                dst = int(chunk[2].replace("D", ""))
                index_dst_list.append((index, dst))
                srcs = list()
                for index_dst in index_dst_list:
                    if index_dst[1] == index:
                        srcs.append(str(index_dst[0]))
                if not srcs:
                    srcs.append(str(-1))
            else:
                surface, morph = line.split("\t")
                morph_list = morph.split(",")
                base, pos, pos1 = (morph_list[6], morph_list[0], morph_list[1])
                morphs.append(Morph(surface, base, pos, pos1))

        else:
            dst = str(dst)
            one_sent_list.append(Chunk(morphs, dst, srcs))
            morphs = list()
            all_sent_list.append(one_sent_list)
            one_sent_list = list()
            index_dst_list = list()
            return_chunk_flag = False

    return all_sent_list


def main():
    fin = open(sys.argv[1], "r")
    all_sent_list = make_chunk_class(fin)
    fin.close()
    for chunk in all_sent_list[7]:
        for morph in chunk.morphs:
            print "\t".join((morph.surface, morph.base, morph.pos, morph.pos1))
        print "係り受け先:\t" + chunk.dst
        print "係り受け元:\t" + ", ".join(chunk.srcs)


if __name__ == "__main__":
    main()
