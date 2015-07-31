#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import pickle


def coo_count(f):
    word_dic = {}
    cont_dic = {}
    coo_dic = {}
    all_count = 0
    for line in f:
        (t,c) = line.strip().split("\t")
        if t in word_dic:
            word_dic[t] += 1
        else:
            word_dic[t] = 1
        if c in cont_dic:
            cont_dic[c] += 1
        else:
            cont_dic[c] = 1
        if t in coo_dic:
            if c in coo_dic[t]:
                coo_dic[t][c] += 1
            else:
                coo_dic[t][c] = 1
        else:
            coo_dic[t] = {}
        all_count += 1

    return word_dic, cont_dic, coo_dic, all_count



if __name__ == "__main__":
    f = open("context.txt", "r")
    (word_dic, cont_dic, coo_dic, all_count) = coo_count(f)
    print len(word_dic), len(cont_dic), len(coo_dic), all_count
    print coo_dic.items()[0]

    f_word = open("word_dic.pcl", "w")
    f_cont = open("cont_dic.pcl", "w")
    f_coo = open("coo_dic.pcl", "w")
    pickle.dump(word_dic, f_word)
    pickle.dump(cont_dic, f_cont)
    pickle.dump(coo_dic, f_coo)

    f_N = open("N.txt", "w")
    f_N.write(str(all_count))
