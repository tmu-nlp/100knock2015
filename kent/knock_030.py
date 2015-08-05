#!/usr/bin/python
#-*-coding:utf-8-*-

import urllib2
import MeCab
from collections import defaultdict

def make_mecab_list():

    d = defaultdict(lambda:0)
    f = open("neko.txt.mecab", "r")
    s_list = []
    mecab_list = []

    #d, listの中へ入れる作業
    for line in f:
        line = line.replace("\t", ",")
        line = line.strip().split(",")
        if line[0] == "EOS":
            mecab_list.append(s_list)
            s_list = []
            continue

        d["surface"] = line[0]
        d["base"] = line[7]
        d["pos"] = line[1]
        d["pos1"] = line[2]
        s_list.append(d.copy())

    return mecab_list

if __name__ == "__main__":
    m = make_mecab_list()

    for i in m:
        for j in i:
            print len(j)
