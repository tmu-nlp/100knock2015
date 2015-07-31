#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import sklearn.decomposition as deco


# sklearn にある諸々の PCA は密行列しか引数に取れないので、PCA に似た
# アルゴリズムの SVD を使う


def pca(matrix, dim):
    pca = deco.TruncatedSVD(n_components = dim)
    pca.fit(matrix)
    reduced_matrix = pca.transform(matrix)
    np.save("context_matrix_reduced", reduced_matrix)



if __name__ == "__main__":
    sp_matrix = np.load("context_matrix.npy")
    print sp_matrix
    pca(sp_matrix, 300)
