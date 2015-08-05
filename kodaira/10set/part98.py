#!usr/bin/python 



import pickle
import numpy
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

if __name__ == '__main__':
    count_names, count_vec = pickle.load(open('country_data.pkl') )
    vec_linkage = linkage(pdist(numpy.array(count_vec) ) )
    dendrogram(vec_linkage, labels = count_names)
    plt.savefig('part98.png')
