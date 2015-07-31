#!/usr/bin/python
# -*- coding:utf-8 -*-

import re
from xml.etree import ElementTree


def extr_np(s_exp):
    pattern = re.compile(r"\([^()]+\)")
    words = pattern.findall(s_exp)
    s_exp = pattern.sub(lambda x:x.group()[1:-1].split(" ")[1], s_exp)

    pattern = re.compile(r"\(NP[^()]+\)")
    lst = []
    while True:
        nps = pattern.findall(s_exp)
        if len(nps) == 0:
            break
        lst += map(lambda x:x[4:-1], nps)
        s_exp = pattern.sub(lambda x:" ".join(x.group()[1:-1].split(" ")[1:]), s_exp)

    for np in lst:
        print np



if __name__ == "__main__":
    f = "nlp.txt.xml"
    tree = ElementTree.parse(f)
    root = tree.getroot()
    parses = [p.text for p in root.findall(".//parse")]
    for parse in parses[:1]:
        extr_np(parse)
