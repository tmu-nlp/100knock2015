#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


def cul_acc(data):
    tp = 0; all_ins = 0
    for line in data:
        line = line.strip()
        values = line.split(" ")
        if values[3] == values[4]:
            tp += 1
        all_ins += 1

    print tp / float(all_ins)


if __name__ == "__main__":
    data = open("eval_instances_new.txt", "r").readlines()
    cul_acc(data)
