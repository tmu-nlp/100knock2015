#!usr/bin/python
#coding:utf-8

import pickle
import numpy as np
from collections import defaultdict
from part87 import *

def main():
    matrix,t_set = pickle.load(open('part85.dump'))
    t_set = list(t_set)
    index_Englanad = t_set.index('England')
    sim_dict = dict()
    count = 0
    for index in range(9999):
        cos_sim = cal_cos_sim(matrix,index,index_Englanad)
        sim_dict[t_set[index]] = cos_sim
    for key,value in sorted(sim_dict.items(),key = lambda x:-x[1]):
        count += 1
        if count > 10:
            break
        print key,value


if __name__ == '__main__':
    main()
