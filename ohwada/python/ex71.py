#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


f_sw = open("/Users/oowadakenichi/nltk_data/corpora/stopwords/english", "r")
sw_lst = [w.strip() for w in f_sw.readlines()]


def is_stop_word(word):    
    if word in sw_lst:
        return True
    else:
        return False 


def test():
    c = 0
    if is_stop_word("run"):
        print "error"
    else:
        print "pass"
        c += 1
    if is_stop_word("have"):
        print "pass"
        c += 1
    else:
        print "error"
    if c == 2:
        print "pass all"



if __name__ == "__main__":
    
    test()
