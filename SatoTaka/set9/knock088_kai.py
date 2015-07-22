#!/usr/bin/python
# _*_ coding:utf-8 _*_

import pickle
import numpy as np
from knock087 import cos_sim
from collections import defaultdict

def make_sim_dict(word_context_matrix, word_set, objective_word, word_dict):
    
    Index_specific_word = word_set.index(objective_word)
    objective_representation = word_context_matrix[Index_specific_word]
    # 受け取った単語のベクトル表現

    for index, word in enumerate(word_set):
        if word == objective_word:
           continue
        else:
           sim = cos_sim(word_context_matrix[index], objective_representation)
           word_dict[word] = sim
    return word_dict

def main():
    t_c_matrix = open("t_c_matrix", "r")
    t_set      = open("t_set", "r")
    word_dict  = defaultdict(float)

    word_context_matrix = pickle.load(t_c_matrix)
    word_set = pickle.load(t_set)
    word_set = list(word_set)

    word_dict = make_sim_dict(word_context_matrix, word_set, "England", word_dict)

    count = 0
    for word, sim in sorted(word_dict.items(), key = lambda x:-x[1]):
        print word + "\t" + str(sim)
        count += 1
        if count == 9:
           break
if __name__=="__main__":
   main()
