# coding: utf-8

import kn30 as senbei
import kn36 as senbei2
import matplotlib.pyplot as plt
from collections import defaultdict


def make_topten_graph(word2freq):
    X_str = list()
    Y = list()
    X = list()
    count = 1
    for word, freq in sorted(word2freq.items(), key=lambda x: x[1], reverse=True):
        X_str.append(word.decode("utf-8"))
        Y.append(freq)
        X.append(count)
        count += 1
        if count > 10:
            break
    plt.bar(X, Y, align="center")
    plt.xticks(X, X_str)
    plt.show()


def main():
    fin = open("neko.txt.mecab", "r")
    morph_mapping_lists = senbei.make_morph_mapping_lists(fin)
    fin.close()
    word2freq = senbei2.make_word2freq(morph_mapping_lists)
    make_topten_graph(word2freq)


if __name__ == "__main__":
    main()
