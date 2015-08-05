#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
import knock30 as takayuki
from collections import defaultdict

def main():
    
    mecab_file = open(sys.argv[1], "r")
    all_sentences = takayuki.make_morphdicts(mecab_file)
    mecab_file.close()

    count_word = defaultdict(lambda: 0)

    for one_sentence in all_sentences:
        for morphdict in one_sentence:
            count_word[morphdict["base"]] += 1

    for word, count in sorted(count_word.items(), key = lambda x:-x[1]):
        print word + "\t" + str(count)


if __name__ == "__main__": 
   main()
