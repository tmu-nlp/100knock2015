#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from ex74 import *


# モデルと訓練ファイルからラベルを予測し出力
def predict(data, model):
    for line in data:
        line = line.strip()
        true_label = line.split(" ")[0]
        (pred_label, prob, feat_line) = label_and_prob(line, model)
        print "\t".join(map(lambda x:str(x), [true_label, pred_label, prob]))   


# classias-tag の出力を整形
def output(lines):
    for line in lines:
        line = line.strip()
        true_label = line.split(" ")[0]
        (pred_label, prob) = line.split(" ")[1].split(":")
        print "\t".join([true_label, pred_label, prob])


if __name__ == "__main__":
    data = open(sys.argv[1], "r")
    model = open(sys.argv[2], "r")
    predict(data, model)

    #lines = sys.stdin
    #output(lines)         
