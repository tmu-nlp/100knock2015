# coding:utf-8

import subprocess
from kajiwara_40 import Morph


class Chunk:
    def __init__(self, phrase_number, phrases, relations):
        self.morphs = [Morph(line) for line in phrases[phrase_number]]
        self.dst = relations[phrase_number][-1]
        self.srcs = [source for source, destination in relations if destination == phrase_number]
        if not self.srcs:
            self.srcs = [-1]

    def is_nominal_phrase(self):
        if [morph.pos for morph in self.morphs if morph.pos == "名詞"]:
            return True
        else:
            return False


def renew_phrase(phrase, phrases):
    if phrase:
        phrases.append(phrase)
        phrase = list()
    return phrase, phrases


def get_chunks_list(fname):
    fin = open(fname, "r")
    phrase = list()
    phrases = list()
    relations = list()
    sentences = list()
    for line in fin:
        if line.startswith("* "):
            phrase, phrases = renew_phrase(phrase, phrases)
            relations.append(tuple([int(number.replace("D", "")) for number in line.strip().split(" ")[1:3]]))
        elif line == "EOS\n":
            phrase, phrases = renew_phrase(phrase, phrases)
            sentences.append([Chunk(phrase_number, phrases, relations) for phrase_number in range(len(relations))])
            phrases = list()
            relations = list()
        else:
            phrase.append(line)
    fin.close()
    return sentences


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.cabocha"
    dname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/"
    sentences = get_chunks_list(fname)
    for sentence_number in range(len(sentences)):
        for phrase_number in range(len(sentences[sentence_number])):
            if not sentences[sentence_number][phrase_number].is_nominal_phrase():
                continue
            outputs = ["".join([morph.surface for morph in sentences[sentence_number][phrase_number].morphs])]
            while not sentences[sentence_number][phrase_number].dst == -1:
                outputs.append("".join([morph.surface for morph in sentences[sentence_number][sentences[sentence_number][phrase_number].dst].morphs]))
                phrase_number = sentences[sentence_number][phrase_number].dst
            print " -> ".join(outputs)


if __name__ == '__main__':
    main()
