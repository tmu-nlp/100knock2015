# coding:utf-8

import kajiwara_30 as mogura
import kajiwara_36 as mogu_count
import matplotlib.pyplot as plot
from collections import defaultdict


def main():
    fin = open("/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.mecab", "r")
    morph_lists = mogura.get_morphs(fin)
    fin.close()
    word2freq = mogu_count.word_count(morph_lists)
    plot.plot(range(len(word2freq.keys())), [freq for word, freq in sorted(word2freq.items(), key=lambda x: x[1], reverse=True)])
    plot.xscale("log")
    plot.yscale("log")
    plot.show()


if __name__ == '__main__':
    main()
