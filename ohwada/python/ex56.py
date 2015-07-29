#!/usr/bin/python
# -*- coding:utf-8 -*-

import subprocess
from xml.etree import ElementTree


def extr_coreference(xml):
    tree = ElementTree.parse(xml)
    root = tree.getroot()

    sentences = root.findall(".//sentence")
    sent_lst = []
    for sent in sentences:
        sent = " ".join(map(lambda x:x.text, sent.findall(".//word")))
        sent_lst.append(sent)
    coreferences = root.findall(".//coreference")

    for coref in coreferences[1:]:
        repre = coref[0].find("text").text
        for mention in coref[1:]:
            sent_id = mention.find("sentence").text
            anp = mention.find("text").text
            sent = sent_lst[int(sent_id)-1]
            print sent.replace(anp, "「" + anp + " ( " + repre + " ) " + "」") + "\n"


if __name__ == "__main__":
    f = "nlp.txt.xml"
    extr_coreference(f)
