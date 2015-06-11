# coding:utf-8

"""
brew install gts
brew install graphviz
sudo pip install pydot
sudo pip install graphviz
"""

import pydot
import subprocess
from kajiwara_41 import get_chunks_list


def write_jpeg(edges, fname):
    graph = pydot.graph_from_edges(edges)
    graph.write_jpeg(fname, prog="dot")


def main():
    sentence_number = 7
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.cabocha"
    sentences = get_chunks_list(fname)
    edges = list()
    for phrase_number in range(len(sentences[sentence_number])):
        destination_number = sentences[sentence_number][phrase_number].dst
        if destination_number == -1:
            continue
        original_phrase = "".join([morph.surface for morph in sentences[sentence_number][phrase_number].morphs])
        destination_phrase = "".join([morph.surface for morph in sentences[sentence_number][destination_number].morphs])
        edges.append((original_phrase, destination_phrase))
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/relations.jpg"
    write_jpeg(edges, fname)
    subprocess.call("open " + fname, shell=True)


if __name__ == '__main__':
    main()
