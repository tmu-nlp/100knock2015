#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import re

f = open("article_uk.txt", "r")

doc = f.read()

match = re.search(r"{{基礎情報.+^}}", doc, re.MULTILINE | re.DOTALL)
template = match.group()

l = template[2:-2].split("\n|")[1:]

d = {}
for val in l:
    (field, value) = map(lambda x: x.strip(), val.split(" = "))
    value = re.sub(r"'{2,4}", "", value)
    d[field] = value
    print field, value
