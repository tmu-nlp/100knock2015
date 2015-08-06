#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib.pyplot as plt


def ward_method(data):
    ward_clusters = ward(data)
    dendrogram(ward_clusters)
    plt.show()


if __name__ == "__main__":
    # ex98, ex99 は、サーバで動かす場合は ssh -X ... でサーバに入らないとエラーが出る
    data = np.load("country_vectors.npy")
    ward_method(data)
