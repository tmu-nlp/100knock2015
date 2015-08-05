#!/usr/bin/python
#_*_coding:utf-8_*_

from collections import defaultdict


def macab_make_list():

    input_file = open("neko.txt.mecab", "r")
    dict_morpho = defaultdict(lambda: 0)
    sentence_list = []
    mecab_list = []

    for line in input_file:
        line = line.replace("\t", ",")
        line = line.strip().split(",")
        #for i in line:
        #    print i
        if line[0] == "EOS":
            mecab_list.append(sentence_list)
            sentence_list = []
            continue

        dict_morpho["surface"] = line[0]
        dict_morpho["base"] = line[7]
        dict_morpho["pos"] = line[1]
        dict_morpho["pos1"] = line[2]
        sentence_list.append(dict_morpho.copy())

    return mecab_list


if __name__ == "__main__":
    m = macab_make_list()

    for sentence_list in m:
        for index, dict_morpho in enumerate(sentence_list):
            if dict_morpho["pos"] == "助詞" and dict_morpho["pos1"] == "連体化":
                print sentence_list[index - 1]["surface"] \
                    + sentence_list[index]["surface"] \
                    + sentence_list[index + 1]["surface"]
