#!/usr/bin/python
# -*- coding:utf-8 -*-

import pickle
from math import log
import numpy as np
from scipy.sparse import coo_matrix


def context_matrix(coo_dic, word_dic, cont_dic, N):
    row = []
    col = []
    data = []
    conts = cont_dic.keys()
    word_index = 0
    for word, dic in coo_dic.items():
        word_count = word_dic[word]
        for cont, coo in dic.items():
            if coo >= 10:
                ppmi = max(log((coo * N * 1.0)  / (word_count * cont_dic[cont]), 2),
                           0)
            else:
                ppmi = 0

            if ppmi != 0:
                row.append(word_index)
                col.append(conts.index(cont))
                data.append(ppmi)

        word_index += 1
        if word_index/20000.0 in range(1,25):
            print word_index

    row = np.array(row)
    col = np.array(col)
    data = np.array(data)

    sp_matrix = coo_matrix((data, (row, col)))
    np.save("context_matrix", sp_matrix)



if __name__ == "__main__":
    f_word = open("word_dic.pcl", "r")
    f_cont = open("cont_dic.pcl", "r")
    f_coo = open("coo_dic.pcl", "r")
    f_N = open("N.txt", "r")
    word_dic = pickle.load(f_word)
    cont_dic = pickle.load(f_cont)
    coo_dic = pickle.load(f_coo)
    N = int(f_N.read())

    context_matrix(coo_dic, word_dic, cont_dic, N)
