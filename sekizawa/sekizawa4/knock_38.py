#!usr/bin/python
#coding:utf-8

import matplotlib.pyplot as plt
import knock_36
from collections import defaultdict

if __name__ == "__main__":
    dic = knock_36.freq()
    value_list = []
    count = 0
    for value in dic.values():
        value_list.append(value)

    plt.hist(value_list, bins = 200, range = (0, 20000))
    plt.show()


