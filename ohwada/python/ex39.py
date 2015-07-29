#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import pickle
from collections import Counter
from ex30 import read_mecab
import matplotlib.pyplot as plt


def plot(dic):
    freq = sorted(freq_dic.values(), reverse=True)
    plt.plot(range(1, len(freq)+1), freq)
    #freq_rev_lst =  sorted(dic.keys(), reverse=True)
    #plt.plot(range(1, len(freq_rev_lst)+1), freq_rev_lst)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()

if __name__ == "__main__":
    with open("freq_dic.pcl", "r") as f:
        freq_dic = pickle.load(f)

    #dic = Counter(freq_dic.values())
    plot(freq_dic)
