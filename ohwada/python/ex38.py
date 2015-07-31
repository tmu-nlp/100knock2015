#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import pickle
from collections import Counter
from ex30 import read_mecab
import matplotlib.pyplot as plt


def plot(dic):
    print dic
    plt.bar(dic.keys(), dic.values(), align="center")
    plt.show()

if __name__ == "__main__":
    with open("freq_dic.pcl", "r") as f:
        freq_dic = pickle.load(f)

    dic = Counter(freq_dic.values())  # dic -> {freq:count}
    plot(dic)
