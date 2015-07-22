#!/usr/bin/python
# _*_ coding:utf-8 _*_

import pickle
import numpy as np
import math
from collections import defaultdict
import pickle

def main():
    read_file_t_and_c = open("count_t_and_c.txt", "r")
    read_file_t       = open("count_t", "r")
    read_file_c       = open("count_c", "r")
    pickle_file_t_and_c = pickle.load(read_file_t_and_c)
    pickle_file_t       = pickle.load(read_file_t)
    pickle_file_c       = pickle.load(read_file_c)
    t_c_matrix          = open("t_c_matrix", "w")
    t_set_store         = open("t_set", "w")
    
    t_set = set()
    c_set = set()
    PPMI = defaultdict(lambda:defaultdict(int))

    for word in pickle_file_t_and_c.keys():
        for context in pickle_file_t_and_c[word].keys():
            if pickle_file_t_and_c[word][context] >= 10:
 #              print pickle_file_t_and_c[word][context]
               PPMI[word][context] = max(math.log(3048773*pickle_file_t_and_c[word][context]/ \
                                                  float((pickle_file_t[word]*pickle_file_c[context]))), 0) # 3048773はknock082のcount_N
               t_set.add(word)
               c_set.add(context)
            else:
               PPMI[word][context] = 0
    flag = 0
    for word in t_set:
        if flag == 0: # 最初の一回のみ
           Matrix = np.array([[PPMI[word][context] for context in c_set]])
           True_Matrix = Matrix
           flag += 1
        else:
           Matrix = np.array([[PPMI[word][context] for context in c_set]])
           True_Matrix = np.r_[True_Matrix, Matrix]

    print True_Matrix
    pickle.dump(True_Matrix, t_c_matrix)
    pickle.dump(t_set, t_set_store)

    read_file_t_and_c.close()
    read_file_t.close()
    read_file_c.close()
    t_c_matrix.close() 
    t_set_store.close()

if __name__=="__main__":
   main()
