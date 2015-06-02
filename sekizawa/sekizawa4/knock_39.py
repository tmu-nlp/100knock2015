#!usr/bin/python
#coding:utf-8

import matplotlib.pyplot as plt
import knock_36
from collections import defaultdict

if __name__ == "__main__":
    dic = knock_36.freq()
    rank_list = []
    freq_list = []
    rank = 0
    for value in sorted(dic.values(), reverse = True):
        rank += 1
        rank_list.append(rank)
        freq_list.append(value)

    plt.plot(rank_list, freq_list)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()


