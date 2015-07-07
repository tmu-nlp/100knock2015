# coding:utf-8

import subprocess
import xml.etree.ElementTree as ET


def parse_corenlp(fname):
    corenlp_dir = "/Users/moguranosenshi/Downloads/stanford-corenlp-full-2015-04-20/"
    subprocess.call("sh "+corenlp_dir+"corenlp.sh -file "+fname, shell=True)
    subprocess.call("mv "+fname.split("/")[-1]+".xml "+fname+".xml", shell=True)
    return fname+".xml"


def split_word(fname):
    tree = ET.parse(fname)
    root = tree.getroot()
    return [element.text for element in root.findall(".//word")]


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/nlp.txt"
    fname = parse_corenlp(fname)
    words = split_word(fname)
    print "\n".join(words)


if __name__ == '__main__':
    main()
