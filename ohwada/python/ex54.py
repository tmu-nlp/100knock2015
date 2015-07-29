#!/usr/bin/python
# -*- coding:utf-8 -*-

from xml.etree import ElementTree


def extr_wordinfo(xml):
    tree = ElementTree.parse(xml)
    root = tree.getroot()

    tokens = root.findall(".//token")

    for token in tokens:
        word = token.find("word")
        lemma = token.find("lemma")
        pos = token.find("POS")
        print "\t".join([word.text, lemma.text, pos.text])



if __name__ == "__main__":
    f = "nlp.txt.xml"
    extr_wordinfo(f)
