#!/usr/bin/python
#_*_coding:utf-8_*_

from collections import defaultdict


def macab_make_list():

    input_file = open("neko.txt.mecab", "r")
    dict_morpho = defaultdict(lambda: 0)
    sentense_list = []
    mecab_list = []

    for line in input_file:
        line = line.replace("\t", ",")
        line = line.strip().split(",")
        #for i in line:
        #    print i
        if line[0] == "EOS":
            mecab_list.append(sentense_list)
            sentense_list = []
            continue

        dict_morpho["surface"] = line[0]
        dict_morpho["base"] = line[7]
        dict_morpho["pos"] = line[1]
        dict_morpho["pos1"] = line[2]
        sentense_list.append(dict_morpho.copy())

    return mecab_list

if __name__ == "__main__":

    m = macab_make_list()
    counts_word = defaultdict(lambda: 0)

    for sentense_list in m:
        for dict_morpho in sentense_list:
            counts_word[dict_morpho["base"]] += 1

    for key, value in enumerate(sorted(counts_word.items(), key=lambda x: -x[1])):
        print key, value
