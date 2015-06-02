# coding:utf-8

from kajiwara_40 import Morph


class Chunk:
    def __init__(self, phrase_number, phrases, relations):
        self.morphs = [Morph(line) for line in phrases[phrase_number]]
        self.dst = relations[phrase_number][-1]
        self.srcs = [source for source, destination in relations if destination == phrase_number]
        if not self.srcs:
            self.srcs = [-1]


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
    sentences = get_chunks_list(fname)
    for phrase_number, phrase in enumerate(sentences[7]):
        print str(phrase_number) + ": " + " ".join([morph.surface for morph in phrase.morphs]) + "\tdst:" + str(phrase.dst) + "\tsrc:" + ",".join([str(source) for source in phrase.srcs])


if __name__ == '__main__':
    main()
