#!/usr/bin/python
# -*- coding:utf-8 -*-

from xml.etree import ElementTree


def extr_person_name(xml):
    tree = ElementTree.parse(xml)
    root = tree.getroot()

    tokens = root.findall(".//token")

    for token in tokens:
        word = token.find("word")
        ner = token.find("NER")
        if ner.text == "PERSON":
            print word.text


if __name__ == "__main__":
    f = "nlp.txt.xml"
    extr_person_name(f)
