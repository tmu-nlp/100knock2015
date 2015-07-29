#!/usr/bin/python
# -*- coding:utf-8 -*-

from ex40 import Morph


class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def surface(self):
        return "".join([m.surface for m in self.morphs if m.pos != "記号"])

    def is_np(self):
        return "名詞" in [m.pos for m in self.morphs]

    def replace_np(self, cap):
        return cap + [m for m in self.morphs if m.pos != "記号"][-1].surface



def sent_to_chunk_lst(cabocha_file):

    sent_lst = []
    chunk_lst = []

    morphs_lst = []
    morphs = []
    dst_lst = []

    for line in cabocha_file:
        line = line.strip()
        if line[:2] == "* ":
            values = line.split(" ")
            dst_lst.append(int(values[2][:-1]))
            if len(morphs) != 0:
                morphs_lst.append(morphs)
                morphs = []

        elif line == "EOS":
            if len(morphs) != 0:
                morphs_lst.append(morphs)
                morphs = []
                for i in range(len(dst_lst)):
                    srcs = []
                    for j in range(len(dst_lst)):
                        if dst_lst[j] == i:
                            srcs.append(j)
                    chunk_lst.append(Chunk(morphs_lst[i], dst_lst[i], srcs))

                sent_lst.append(chunk_lst)
                morphs_lst = []
                dst_lst = []
                chunk_lst = []

        else:
            (surface, features) = line.split("\t")
            features = features.split(",")
            (base, pos, pos1) = (features[6], features[0], features[1])
            morphs.append(Morph(surface, base, pos, pos1))            


    return sent_lst



if __name__ == "__main__":
    with open("neko.txt.cabocha", "r") as f:
        sent_lst = sent_to_chunk_lst(f)

    for chunk in sent_lst[7]:
        string = "".join([m.surface for m in chunk.morphs])
        print string, chunk.dst
