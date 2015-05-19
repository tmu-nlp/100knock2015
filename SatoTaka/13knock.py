#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys

yomikomi_1 = open(sys.argv[1], "r")
yomikomi_2 = open(sys.argv[2], "r")

kakikomi = open("col3.txt", "w")

for y_1, y_2 in zip(yomikomi_1, yomikomi_2):
    y_1 = y_1.strip()
    y_2 = y_2.strip()
    sentence = y_1 + "\t" + y_2
    kakikomi.write("%s\n" % sentence)


