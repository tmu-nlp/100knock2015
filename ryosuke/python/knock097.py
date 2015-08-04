# coding:utf-8
"""
python knock097.py ../Data/result/knock096/python/country.pkl
"""

import sys
import pickle
import numpy as np
from sklearn.cluster import KMeans

dic = pickle.load(open(sys.argv[1]))

features = np.array(dic.values())
km_model = KMeans(n_clusters=5).fit(features)

for label, name in sorted(zip(km_model.labels_, dic.keys()), key=lambda x: x[0]):
    print label, name

