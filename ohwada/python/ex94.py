#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from gensim.models import word2vec


def cul_sim(data, model):

    f_out = open("set1_sim_word2vec.txt", "w")

    for line in data[1:]:
        line = line.strip()
        (word1, word2) = line.split("\t")[:2]
        try:
            sim = model.similarity(word1, word2)
            new_line = line + "\t" + str(sim) + "\n"
            f_out.write(new_line)
        except:
            pass


if __name__ == "__main__":
    # WordSimilarity-353 Test Collection の評価データ
    data = open("set1.tab", "r").readlines()
    model = word2vec.Word2Vec.load_word2vec_format("vectors.bin", binary=True)
    cul_sim(data, model)
