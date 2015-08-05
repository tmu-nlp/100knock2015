#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import pickle
from ex30 import read_mecab
import matplotlib.pyplot as plt


def plot(lst):
    plt.bar(range(1,11), map(lambda x:x[1], lst), align="center")    
    plt.show()

if __name__ == "__main__":
    with open("freq_dic.pcl", "r") as f:
        freq_dic = pickle.load(f)

    top10 = sorted(freq_dic.items(), key=lambda x:x[1], reverse=True)[:10]
    plot(top10)
