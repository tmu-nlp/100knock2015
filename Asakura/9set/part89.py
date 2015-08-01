#!usr/bin/python
#coding:utf-8

import pickle
from part85 import *
import numpy as np
import math


def cal_cos_sim(matrix,index,vector):
    cos_sim = np.dot(matrix[index],vector)/(math.sqrt(sum(element**2 for element in matrix[index]))* math.sqrt(sum(element**2 for element in vector)))
    return cos_sim


def main():
    matrix, t_set = pickle.load(open('part85.dump'))
    t_set = list(t_set)
    vector = matrix[t_set.index('Spain')] - matrix[t_set.index('Madrid')] + matrix[t_set.index('Athens')]
    sim_dict = dict()
    count = 0
    for index in range(9999):
        cos_sim = cal_cos_sim(matrix,index,vector)
        sim_dict[t_set[index]] = cos_sim
    for key,value in sorted(sim_dict.items(),key = lambda x:-x[1]):
        count += 1
        if count > 10:
            break
        print key,value
if __name__ == '__main__':
    main()
