#!/usr/bin/python
# _*_ coding:utf-8 _*_ 

import pickle
import numpy as np
import math

def cos_sim(m1, m2):
    
    bunbo1 = math.sqrt(sum([each_youso**2 for each_youso in m1]))
    bunbo2 = math.sqrt(sum([each_youso**2 for each_youso in m2]))
   
    return np.dot(m1,m2) / (bunbo1*bunbo2)

def main():
    t_c_matrix = open("t_c_matrix", "r")
    t_set      = open("t_set", "r")

    word_context_matrix = pickle.load(t_c_matrix)
    word_set = pickle.load(t_set)
    word_set = list(word_set)
    

    # word_context_matrixのリスト番号と、word_setのインデックス番号は一致
    Index_UnitedStates = word_set.index("United_States")
    Index_US           = word_set.index("England")

    print  cos_sim(word_context_matrix[Index_UnitedStates], \
                   word_context_matrix[Index_US])
    
    t_c_matrix.close()
    t_set.close()
 
if __name__=="__main__":
   main()
