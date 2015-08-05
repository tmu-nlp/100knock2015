#!/usr/bin/python
# _*_ coding:utf-8 _*_

import pickle
import numpy as np
from knock087 import cos_sim
from collections import defaultdict

def main():
    t_c_matrix = open("t_c_matrix", "r")
    t_set      = open("t_set", "r")
    word_dict  = defaultdict(float)

    word_context_matrix = pickle.load(t_c_matrix)
    word_set = pickle.load(t_set)
    word_set = list(word_set)

    Index_specific_word = word_set.index("England")
    England_representation = word_context_matrix[Index_specific_word]
    # "England"の単語表現

    for index, word in enumerate(word_set):
        if word == "England":
           continue
        else:
#           print England_representation
#           print word_context_matrix[index]
#           print word, 
           sim = cos_sim(England_representation, word_context_matrix[index])
           word_dict[word] = sim
    count = 0
    for word, sim in sorted(word_dict.items(), key = lambda x:-x[1]):
        print word + "\t" + str(sim)
        count += 1
        if count == 9:
           break
if __name__=="__main__":
   main()
