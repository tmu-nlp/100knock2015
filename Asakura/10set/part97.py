#!/usr/bin/python
#coding:utf-8

import pickle
import numpy as np
from sklearn.cluster import KMeans


if __name__ == '__main__':
    country_dict = pickle.load(open('matrix_dict.dump'))
    features = np.array([vector for key,vector in country_dict.items()])
#    print features
    kmeans_model = KMeans(n_clusters=5, random_state=10).fit(features)
    labels = kmeans_model.labels_
    for label, feature in zip(labels, country_dict.keys()):
        print (label, feature)
