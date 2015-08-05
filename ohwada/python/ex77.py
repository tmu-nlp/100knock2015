#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import subprocess


def cul_score(lines):
    tp = 0; fp = 0; fn = 0; tn = 0
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        (ans, pred, prob) = line.split("\t")

        if ans == pred:
            if ans == "+1":
                tp += 1
            else:
                tn += 1
        else:
            if ans == "+1":
                fn += 1
            else:
                fp += 1


    accuracy = (tp+tn) / float(tp+tn+fn+fp)
    precision = tp / float(tp+fp)
    recall = tp / float(tp+fn)
    f1 = 2 * precision * recall / (precision + recall)
    print "accuracy", accuracy
    print "precision", precision
    print "recall", recall
    print "f1", f1


if __name__ == "__main__":
    f = open("output_ex76.txt", "r")
    lines = f.readlines()
    cul_score(lines)
