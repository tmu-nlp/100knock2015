#!/usr/bin/python
#_*_coding:utf-8_*_


from collections import defaultdict


def make_MeCab_list():
    input_MeCab_file = open("neko.txt.mecab", "r")
    dict_morph = defaultdict(lambda: 0)
    MeCab_list = []
    senense_list = []

    for line in input_MeCab_file:
        line = line.replace("\t", ",")
        words = line.strip().split(",")

        if words[0] == "EOS":
            MeCab_list.append(senense_list)
            senense_list = []
            continue

        dict_morph["surface"] = words[0]
        dict_morph["base"] = words[7]
        dict_morph["pos"] = words[1]
        dict_morph["pos1"] = words[2]

        senense_list.append(dict_morph.copy())

    return MeCab_list


if __name__ == "__main__":
    m = make_MeCab_list()

    for i in m:
        for j in i:
            for a, b in j.items():
                print a+":"+b,
            print
