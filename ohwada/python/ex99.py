#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def tSNE(data):
    model = TSNE(n_components=2, random_state=0)
    lst = model.fit_transform(data)

    plt.scatter(lst[:,0], lst[:,1])
    plt.show()


if __name__ == "__main__":
    data = np.load("country_vectors.npy")
    tSNE(data)
