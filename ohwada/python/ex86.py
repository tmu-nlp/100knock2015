#!/usr/bin/python
# -*- coding:utf-8 -*-

import pickle
import numpy as np


word_dic = pickle.load(open("coo_dic2.pcl", "r"))
reduced_matrix = np.load("context_matrix_reduced.npy")


def output_vector(word):
    index = word_dic.keys().index(word)
    vector = reduced_matrix[index]
    return vector


if __name__ == "__main__":
    target_word = "United_States"
    vector = output_vector(target_word)
    print vector
