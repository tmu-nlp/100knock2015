# coding:utf-8

import xml.etree.ElementTree as ET


def get_word_lemma_pos(fname):
    tree = ET.parse(fname)
    root = tree.getroot()
    return [e_word.text+"\t"+e_lemma.text+"\t"+e_pos.text for e_word, e_lemma, e_pos in zip(root.findall(".//word"), root.findall(".//lemma"), root.findall(".//POS"))]


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/nlp.txt.xml"
    tokens = get_word_lemma_pos(fname)
    print "\n".join(tokens)


if __name__ == '__main__':
    main()
