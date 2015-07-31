#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from ex71 import is_stop_word
from stemming.porter2 import stem


def extr_base_features(f):
    feats_lst = []
    for line in f:
        line = line.strip()
        lst = line.split(" ")
        label = lst[0]
        words = lst[1:]
        for word in words:
            if is_stop_word(word):
                words.remove(word)
        line = " ".join([label] + [stem(w) for w in words])
        feats_lst.append(line)

    return feats_lst


def extr_orig_features(f):
    feats_lst = []
    for line in f:
        line = line.strip()
        lst = line.split(" ")
        label = lst[0]
        words = lst[1:]
        features = []
        # bag-of-words
        for word in words:
            if is_stop_word(word):
                words.remove(word)
        features += [stem(w) for w in words]
        # num-of-words
        features.append(str(len(words)))
        # question, exclamation
        if "?" in words:
            features.append("QUES")
        if "!" in words:
            features.append("EXCL")
        line = " ".join([label] + features)
        feats_lst.append(line)

    return feats_lst


if __name__ == "__main__":

    with open("sentiment.txt", "r") as train_f:
        #lst = extr_base_features(train_f)
        feats_lst = extr_orig_features(train_f)

        for features in feats_lst:
            print features
