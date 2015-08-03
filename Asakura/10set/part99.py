#!/usr/bin/python
#coding:utf-8

import pickle
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

if __name__ == '__main__':
    country_dict = pickle.load(open('matrix_dict.dump'))
    matrix = np.array(country_dict.values())
    T_SNE = TSNE().fit_transform(matrix)
    print T_SNE
    x,y = zip(*T_SNE)#例 ([1,2],[3,4],[5,6])→([1,3,5],[2,4,6])
    plt.axis([min(x),max(x),min(y),max(y)])
    for (xx,yy),name in zip(T_SNE,country_dict.keys()):
        plt.text(xx,yy,name)
    plt.show()
