# coding:utf-8

import kajiwara_30 as mogura
from collections import defaultdict


def word_count(morph_lists):
    word2freq = defaultdict(int)
    for morph_list in morph_lists:
        for morph_dict in morph_list:
            word2freq[morph_dict["base"]] += 1
    return word2freq


def main():
    fin = open("/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.mecab", "r")
    morph_lists = mogura.get_morphs(fin)
    fin.close()
    word2freq = word_count(morph_lists)
    for word, freq in sorted(word2freq.items(), key=lambda x: x[1], reverse=True):
        print str(freq) + "\t" + word


if __name__ == '__main__':
    main()
