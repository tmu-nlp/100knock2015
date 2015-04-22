#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


def ngram(sequence, n):
 
    ngram_list = []
   
    for i in range(len(sequence)-(n-1)):
#        ngram_list.append(sequence[i:i+n])
#        ngram_list.append(tuple(sequence[i:i+n]))
        if isinstance(sequence, list) is True:
            ngram_list.append(tuple(sequence[i:i+n]))
        else:
            ngram_list.append(sequence[i:i+n])

    return ngram_list

    
if __name__ == "__main__":
    
    sentence = "I am an NLPer"
    word_list = sentence.split(" ")

    w_bigram_list = ngram(word_list, 2)

    c_bigram_list = []
    for w in word_list:
        c_bigram_list += ngram(w, 2)

    print w_bigram_list
    print c_bigram_list
