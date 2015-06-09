# coding: utf-8

import kn30 as senbei
import kn36 as senbei2
import matplotlib.pyplot as plt
import math
from collections import defaultdict


def make_freq2type(word2freq):
    freq2type = defaultdict(int)
    for word, freq in word2freq.items():
        freq2type[freq] += 1
    return freq2type


def make_histgram(freq2type):
    X_str = list()
    Y = list()
    X = list()
    for freq, types in sorted(freq2type.items(), key=lambda x: x[1], reverse=True):
        Y.append(math.log(freq))
        X.append(math.log(types))
    plt.plot(X, Y)
    plt.show()


def main():
    fin = open("neko.txt.mecab", "r")
    morph_mapping_lists = senbei.make_morph_mapping_lists(fin)
    fin.close()
    word2freq = senbei2.make_word2freq(morph_mapping_lists)
    freq2type = make_freq2type(word2freq)
    make_histgram(freq2type)


if __name__ == "__main__":
    main()
