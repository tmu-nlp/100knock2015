#!/usr/bin/python
#coding:utf-8

import pickle
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

if __name__ == '__main__':
    country_dict = pickle.load(open('matrix_dict.dump'))
    vec_linkage = linkage(pdist(np.array([value for value in country_dict.values()])))
    dendrogram(vec_linkage, labels = country_dict.keys())
    plt.savefig('part98.png')    
