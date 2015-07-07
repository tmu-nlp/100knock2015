#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
import knock30 as takayuki

def main():

    mecab_file    = open(sys.argv[1], "r")
    all_sentences = takayuki.make_morphdicts(mecab_file)
    mecab_file.close()

    for one_sentence in all_sentences:
        for index in range(1, len(one_sentence)):
            if one_sentence[index]["surface"] == "の":
               if one_sentence[index-1]["pos"] == "名詞" and \
                  one_sentence[index+1]["pos"] == "名詞":
                  print one_sentence[index-1]["surface"]\
                        + one_sentence[index]["surface"]\
                        + one_sentence[index+1]["surface"]


if __name__ == "__main__":
   main()
