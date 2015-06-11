# coding:utf-8

import itertools
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
        if [morph.pos for morph in self.morphs if morph.pos == "名詞"] and not [morph.pos for morph in self.morphs if morph.pos == "動詞"]:
            return True
        else:
            return False

    def substitute_nominal_phrase(self, sub):
        outputs = [sub if morph.pos == "名詞" else morph.surface for morph in self.morphs][::-1]
        return "".join(outputs[:outputs.index(sub)+1][::-1])

    def get_all_path(self, sentences, sentence_number):
        chunk_list = list()
        chunk = self
        while True:
            chunk_list.append(chunk)
            if chunk.dst == -1:
                break
            chunk = sentences[sentence_number][chunk.dst]
        return chunk_list


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
    #fin.close()
    return sentences


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.cabocha"
    dname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/"
    sentences = get_chunks_list(fname)
    for sentence_number in range(len(sentences)):
        nominal_phrases = list()
        for phrase_number in range(len(sentences[sentence_number])):
            chunk = sentences[sentence_number][phrase_number]
            if chunk.is_nominal_phrase():
                nominal_phrases.append(chunk)
        for chunk_X, chunk_Y in itertools.combinations(nominal_phrases, 2):
            chunks_X = chunk_X.get_all_path(sentences, sentence_number)
            chunks_Y = chunk_Y.get_all_path(sentences, sentence_number)
            has_nominal_phrase = False
            for i, chunk_X in enumerate(chunks_X):
                if chunk_X in chunks_Y and chunk_X.is_nominal_phrase():
                    has_nominal_phrase = True
                    break
            if has_nominal_phrase:
                outputs = list()
                outputs.append(chunks_X[0].substitute_nominal_phrase("X"))
                outputs.extend(["".join([morph.surface for morph in chunk.morphs]) for chunk in chunks_X[1:i]])
                outputs.append("Y")
                print " -> ".join(outputs)
            else:
                print chunks_X[0].substitute_nominal_phrase("X") + " | " + " -> ".join([chunk.substitute_nominal_phrase("Y") if i == 0 else "".join([morph.surface for morph in chunk.morphs]) for i, chunk in enumerate(chunks_Y[:-1])]) + " | " + "".join([morph.surface for morph in chunks_X[-1].morphs])


if __name__ == '__main__':
    main()
