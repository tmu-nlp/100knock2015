#!/usr/bin/python
# -*- coding:utf-8 -*-


import sys
import pickle


def read_mecab(mecab_file):
    
    sent_lst = []
    morph_lst = []
    keys = ("surface", "base", "pos", "pos1")

    with open(mecab_file, "r") as f:
        for line in f:
            line = line.strip()
            if line == "EOS":
                if len(morph_lst) == 0:
                    continue
                sent_lst.append(morph_lst)
                morph_lst = []
            else:
                (surface, feats) = line.split("\t")
                feats = feats.split(",")
                (base, pos, pos1) = (feats[6], feats[0], feats[1])
                d = dict(zip(keys, (surface, base, pos, pos1)))
                morph_lst.append(d)

    return sent_lst


if __name__ == "__main__":
    sent_lst = read_mecab("neko.txt.mecab")

    with open("sent_lst.pcl", "w") as f:
        pickle.dump(sent_lst, f)
