# coding:utf-8

import xml.etree.ElementTree as ET


def parse_s(s_expression, nps):
    s_expression = s_expression.replace(") (", ")(")
    for words in s_expression.split("(NP ")[1:]:
        np = ""
        for word in words.split("))")[0].split(" ")[1:]:
            np = np + word.split(")")[0] + " "
        np = np.strip()
        if np:
            nps.append(np)
    return nps


def parse_xml(fname):
    nps = list()
    tree = ET.parse(fname)
    for sentence in tree.find(".//sentences").getiterator("sentence"):
        parse = sentence.findtext("parse")
        nps = parse_s(parse, nps)
    return nps


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/nlp.txt.xml"
    nps = parse_xml(fname)
    for np in nps:
        print np


if __name__ == '__main__':
    main()
