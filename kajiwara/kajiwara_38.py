# coding:utf-8

import kajiwara_30 as mogura
import kajiwara_36 as mogu_count
import matplotlib.pyplot as plot
from collections import defaultdict


def count_number_of_difference(word2freq):
    freq2type = defaultdict(int)
    for word, freq in word2freq.items():
        freq2type[freq] += 1
    return [freq for freq, type in sorted(freq2type.items())], [type for freq, type in sorted(freq2type.items())]


def main():
    fin = open("/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.mecab", "r")
    morph_lists = mogura.get_morphs(fin)
    fin.close()
    word2freq = mogu_count.word_count(morph_lists)
    x, y = count_number_of_difference(word2freq)
    plot.bar(x[:30], y[:30])
    plot.show()


if __name__ == '__main__':
    main()
