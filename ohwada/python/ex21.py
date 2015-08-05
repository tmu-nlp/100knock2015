#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


f = open("article_uk.txt", "r")

for line in f:
    if "Category" in line:
        print line.strip()
