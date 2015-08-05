#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import matplotlib.pyplot as plt


def prec_recall_curve(output):
    lst = []
    for line in output:
        line = line.strip()
        (ans, pred, prob) = line.split("\t")
        lst.append((ans, float(prob)))

    pr_lst = []
    thres = 1.0
    while thres >= 0.0:
        tp = 0; fp = 0; fn = 0; tn = 0
        # 閾値より確率が大きい事例について
        for tup in [tup for tup in lst if tup[1] > thres]:
            if tup[0] == "+1":
                tp += 1
            else:
                fp += 1
        # 閾値より確率が小さい事例について
        for tup in [tup for tup in lst if tup[1] < thres]:
            if tup[0] == "+1":
                fn += 1
            else:
                tn += 1

        if tp == 0:
            pass
        else:
            precision = tp / float(tp+fp)
            recall = tp / float(tp+fn)
            pr_lst.append((precision, recall))

        thres -= 0.01

    plot(pr_lst)


def plot(pr_lst):
    precision = [tup[0] for tup in pr_lst]
    recall = [tup[1] for tup in pr_lst]
    plt.plot(recall, precision)
    plt.ylabel("Precision")
    plt.xlabel("Recall")
    plt.show()



if __name__ == "__main__":
    output = open("output_ex76.txt", "r")
    prec_recall_curve(output)
