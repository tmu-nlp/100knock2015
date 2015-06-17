# coding: utf-8

import re


def split_sentence(fname):
    end_of_sentence_pattern = re.compile('(?P<end>\.|\;|\:|\?|\!)\s(?P<start>[A-Z])')
    sentences = list()
    fin = open(fname, "r")
    for line in fin:
        line = line.strip()
        if not line:
            continue
        for sentence in end_of_sentence_pattern.sub(lambda x: '%s\n%s' % (x.group('end'), x.group('start')), line).split("\n"):
            sentences.append(sentence)
    fin.close()
    return sentences


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/nlp.txt"
    sentences = split_sentence(fname)
    print "\n".join(sentences)


if __name__ == '__main__':
    main()
