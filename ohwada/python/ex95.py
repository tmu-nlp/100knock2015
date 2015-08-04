#!/usr/bin/python
# -*- coding:utf-8 -*-


def cul_Spearman(data):
    lst_human = []
    lst_word2vec = []

    for line in data:
        line = line.strip()
        values = line.split("\t")
        word_pair = "/".join(values[:2])
        human_mean = values[2]
        word2vec = values[-1]
        lst_human.append((word_pair, human_mean))
        lst_word2vec.append((word_pair, word2vec))

    sorted_human = [val[0] for val in
                    sorted(lst_human, key=lambda x:x[1], reverse=True)]
    sorted_word2vec = [val[0] for val in
                       sorted(lst_word2vec, key=lambda x:x[1], reverse=True)]
    rank_lst = [sorted_word2vec.index(val) for val in sorted_human]

    i = 0
    s = 0.0
    for val in rank_lst:
        print val, i, s
        s += (val - i) ** 2
        i += 1

    N = len(rank_lst)
    # r: スピアマンの順位相関係数
    r = 1 - (s / (N ** 3 - N))
    
    print r


if __name__ == "__main__":
    # 94. で作ったデータ
    data = open("set1_sim_word2vec.txt", "r")
    cul_Spearman(data)
