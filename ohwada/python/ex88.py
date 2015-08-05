#!/usr/bin/python
# -*- coding:utf-8 -*-

import pickle
import numpy as np
from ex86 import output_vector
from ex87 import cos_simmilarity


word_dic = pickle.load(open("word_dic2.pcl", "r"))
reduced_matrix = np.load("context_matrix_reduced2.npy")


def similar_top10(vector):
    lst = []
    for (i, vec) in enumerate(reduced_matrix):
        print cos_simmilarity(vector, vec)
        lst.append((i, cos_simmilarity(vector, vec)))
    top10_lst = []
    for i, vec in sorted(lst, key=lambda x:x[1], reverse=True)[:10]:
        word = word_dic.keys()[i]
        top10_lst.append((word, vec))

    return top10_lst


if __name__ == "__main__":
    vector = output_vector("England")
    top10_lst = similar_top10(vector)
    for word, vec in top10_lst:
        print word, vec
