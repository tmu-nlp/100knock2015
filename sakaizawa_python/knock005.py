#!/usr/bin/python
# -*- coding:utf-8

#05. n-gram
#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def n_gram(sent, n):
    n_gram_list = []
    for i in range(len(sent)-n+1):
        n_gram_list.append(sent[i:i+n])
    return n_gram_list


if __name__ == "__main__":
    sent = "I am an NLPer"
    word_bi_gram = n_gram(sent.split(), 2)
    char_bi_gram = n_gram(sent, 2)

    print word_bi_gram
    print char_bi_gram




