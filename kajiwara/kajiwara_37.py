# coding:utf-8

import kajiwara_30 as mogura
import kajiwara_36 as mogu_count
import matplotlib.pyplot as plot
from collections import defaultdict


def main():
    num = 10
    fin = open("/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.mecab", "r")
    morph_lists = mogura.get_morphs(fin)
    fin.close()
    word2freq = mogu_count.word_count(morph_lists)
    plot.bar(range(1, num+1), [freq for word, freq in sorted(word2freq.items(), key=lambda x: x[1], reverse=True)][:num], align="center")
    plot.xticks(range(1, num+1), [word.decode("utf-8") for word, freq in sorted(word2freq.items(), key=lambda x: x[1], reverse=True)][:num])
    plot.show()


if __name__ == '__main__':
    main()
