# coding:utf-8

import xml.etree.ElementTree as ET


def get_person(fname):
    tree = ET.parse(fname)
    root = tree.getroot()
    return [e_word.text for e_word, e_ner in zip(root.findall(".//word"), root.findall(".//NER")) if e_ner.text == "PERSON"]


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/nlp.txt.xml"
    names = get_person(fname)
    print "\n".join(names)


if __name__ == '__main__':
    main()
