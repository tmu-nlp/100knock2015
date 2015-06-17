# coding: utf-8

import re
from kajiwara_50 import split_sentence


def split_word(fname):
    mark_pattern = re.compile("\(|\)|,|\.|\?|^'|',|'\.")
    sentences = split_sentence(fname)
    return [mark_pattern.sub("", word.replace('"', "")) for sentence in sentences for word in (sentence+"\n").split(" ")]


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/nlp.txt"
    words = split_word(fname)
    print "\n".join(words)


if __name__ == '__main__':
    main()
