#!usr/bin/python
#coding:utf-8

import pickle
import numpy as np
import math

def cal_cos_sim(matrix,index,index_):
    cos_sim = np.dot(matrix[index],matrix[index_])/(math.sqrt(sum(element**2 for element in matrix[index]))* math.sqrt(sum(element**2 for element in matrix[index_])))
    return cos_sim

def main():
    matrix,t_set = pickle.load(open('part85.dump'))
    t_set = list(t_set)
    index_United_States = t_set.index('United_States')
    index_US = t_set.index('U.S')
    cos_sim = cal_cos_sim(matrix,index_US,index_United_States)
    print cos_sim


if __name__ ==  '__main__':
    main()

