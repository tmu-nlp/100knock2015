# coding:utf-8

from kajiwara_40 import Morph
from collections import defaultdict


class Chunk:
    def __init__(self, phrase_number, phrases, relations):
        self.morphs = [Morph(line) for line in phrases[phrase_number]]
        self.dst = relations[phrase_number][-1]
        self.srcs = [source for source, destination in relations if destination == phrase_number]
        if not self.srcs:
            self.srcs = [-1]


def main():
    fin = open("/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.cabocha", "r")
    phrase = list()
    phrases = list()
    relations = list()
    sentences = list()
    for line in fin:
        if line.startswith("* "):
            if phrase:
                phrases.append(phrase)
                phrase = list()
            relations.append(tuple([int(number.replace("D", "")) for number in line.strip().split(" ")[1:3]]))
        elif line == "EOS\n":
            if phrase:
                phrases.append(phrase)
                phrase = list()
            sentences.append([Chunk(phrase_number, phrases, relations) for phrase_number in range(len(relations))])
            phrases = list()
            relations = list()
        else:
            phrase.append(line)
    fin.close()
    for phrase_number, phrase in enumerate(sentences[7]):
        print str(phrase_number) + ": " + " ".join([morph.surface for morph in phrase.morphs]) + "\tdst:" + str(phrase.dst) + "\tsrc:" + ",".join([str(source) for source in phrase.srcs])


if __name__ == '__main__':
    main()
