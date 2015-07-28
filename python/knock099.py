# coding:utf-8
"""
python knock099.py ../Data/result/knock096/python/country.pkl
"""

import sys
import pickle
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

dic = pickle.load(open(sys.argv[1]))

features = np.array(dic.values())

embeded = TSNE().fit_transform(features)

x, y = zip(*embeded)

plt.plot(zip(*embeded), 'o')
plt.axis([min(x), max(x), min(y), max(y)])
plt.show()
