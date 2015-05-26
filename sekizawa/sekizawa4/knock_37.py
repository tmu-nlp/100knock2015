#!usr/bin/python
#coding:utf-8

import matplotlib.pyplot as plt
import knock_36
from collections import defaultdict

if __name__ == "__main__":
    dic = knock_36.freq()
    count_list = []
    key_list = []
    value_list = []
    count = 0
    for key, value in sorted(dic.items(), key = lambda x:x[1], reverse = True):
        if count < 10:
            count += 1
            count_list.append(count)
            key_list.append(unicode(key, "utf-8"))
            value_list.append(value)
        else:
            break

    plt.bar(count_list, value_list, align = "center")
    plt.xticks(count_list, key_list)
    plt.show()

