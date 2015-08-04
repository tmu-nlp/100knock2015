# coding:utf-8
"""
python knock098.py ../Data/result/knock096/python/country.pkl
"""

import sys
import pickle
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

dic = pickle.load(open(sys.argv[1]))

features = np.array(dic.values())

model = linkage(pdist(features))
dendrogram(model, labels=dic.keys(), orientation='right')
plt.show()

