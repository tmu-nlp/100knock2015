#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.cluster import KMeans


def k_means(data, k):

    model = KMeans(n_clusters=k).fit(data)
    labels = model.labels_
    for vec, label in zip(data, labels):
        #print vec, label
        print label



if __name__ == "__main__":
    data = np.load("country_vectors.npy")
    k_means(data, 5)
