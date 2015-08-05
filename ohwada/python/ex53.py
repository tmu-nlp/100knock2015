#!/usr/bin/python
# -*- coding:utf-8 -*-

from xml.etree import ElementTree


def extr_word(xml):
    tree = ElementTree.parse(xml)
    root = tree.getroot()

    tokens = root.findall(".//token")

    for token in tokens:
        word = token.find("word")
        print word.text



if __name__ == "__main__":
    f = "nlp.txt.xml"
    extr_word(f)
