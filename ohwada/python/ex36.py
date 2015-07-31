#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import pickle
from collections import Counter
from ex30 import read_mecab

def extr(sent_lst):
    
    word_lst = map(lambda d:d["base"], reduce(lambda a,b:a+b,  sent_lst))
    freq_dic = Counter(word_lst)
    for w, f in sorted(freq_dic.items(), key=lambda x:x[1], reverse=True):
        print w, f

    with open("freq_dic.pcl", "w") as f:
        pickle.dump(freq_dic, f)


if __name__ == "__main__":
    sent_lst = read_mecab("neko.txt.mecab")

    extr(sent_lst)
