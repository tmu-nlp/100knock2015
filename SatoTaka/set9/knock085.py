#!/usr/bin/python
# _*_ coding:utf-8 _*_

import pickle
import numpy as np
from sklearn.decomposition import TruncatedSVD

def main():
    
    t_c_matrix = open("t_c_matrix", "r")
    matrix = pickle.load(t_c_matrix)

    decomp = TruncatedSVD(n_components=300)
    decomp.fit(matrix)
    matrix = decomp.transform(matrix)

    print matrix
    
    t_c_matrix.close()

if __name__=="__main__":
   main()
