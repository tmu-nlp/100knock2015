# coding: utf-8

from stemming.porter2 import stem
from kajiwara_51 import split_word


def get_stem(fname):
    words = split_word(fname)
    return [word.strip()+"\t"+stem(word.strip())+"\n" if word.endswith("\n") else word+"\t"+stem(word) for word in words]


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/nlp.txt"
    word_stem_list = get_stem(fname)
    print "\n".join(word_stem_list)


if __name__ == '__main__':
    main()
