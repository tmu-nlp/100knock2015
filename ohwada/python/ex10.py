#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    print len(lines)


# コマンド
# wc -l hightemp.txt
