#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print line.strip().replace("\t", " ")


# コマンド
# sed -e s/$'\t'/' '/g hightemp.txt
# tr '\t' ' ' < hightemp.txt
# expand -t 1 hightemp.txt 
