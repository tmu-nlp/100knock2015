# coding:utf-8

from collections import defaultdict


def main(sentence):
    char2index = defaultdict(int)
    word_list = sentence.replace(".", "").split()
    for i, word in enumerate(word_list, 1):
        if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            char2index[word[0]] = i
        else:
            char2index[word[:2]] = i
    print char2index


if __name__ == '__main__':
    main("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")
