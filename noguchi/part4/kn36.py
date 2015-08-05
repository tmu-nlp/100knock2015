# coding: utf-8

import kn30 as senbei
from collections import defaultdict


def make_word2freq(morph_mapping_lists):
    word2freq = defaultdict(int)
    for morph_mapping_list in morph_mapping_lists:
        for morph_map in morph_mapping_list:
            word2freq[morph_map["base"]] += 1
    return word2freq


def main():
    fin = open("neko.txt.mecab", "r")
    morph_mapping_lists = senbei.make_morph_mapping_lists(fin)
    fin.close()
    word2freq = make_word2freq(morph_mapping_lists)
    for word, freq in sorted(word2freq.items(), key=lambda x: x[1], reverse=True):
        print word + "\t" + str(freq)


if __name__ == "__main__":
    main()
