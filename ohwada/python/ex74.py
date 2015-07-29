#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import math
from ex72 import extr_orig_features


model = open(sys.argv[2], "r")
weight_dic = dict([(l.split("\t")[1].strip(), l.split("\t")[0])
                    for l in model.readlines()[2:]])
bias = float(weight_dic["__BIAS__"])


def label_and_prob(line, model):
    line = line.strip()
    lst = line.split(" ")
    label = lst[0]
    features = lst[1:]
    score = 0
    for feature in features:
        try:
            weight = weight_dic[feature]
            score += float(weight)
        except:
            pass

    prob = sigmoid(score + bias)

    if prob < 0.5:
        label = "-1"
    else:
        label = "+1"

    return label, prob, " ".join(features)


def sigmoid(x):
    s = 1 / (1 + math.exp(-x))
    return s




if __name__ == "__main__":
    data = open(sys.argv[1], "r")
    feats_lst = extr_orig_features(data)    
    for line in feats_lst:
        (label, score, feat_line) = label_and_prob(line, model)
        print label, score, feat_line
