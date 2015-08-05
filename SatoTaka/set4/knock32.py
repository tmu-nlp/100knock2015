#!/usr/bin/python
# _*_ coding:utf-8 _*_

import knock30 as takayuki
import sys

def main():
    
    mecab_file   = open(sys.argv[1], "r")
    all_sentences = takayuki.make_morphdicts(mecab_file)
    mecab_file.close()

    for one_sentence in all_sentences:
        for morphdict in one_sentence:
            if morphdict["pos"] == "動詞":
               print morphdict["base"]


if __name__ == "__main__":
   main()
