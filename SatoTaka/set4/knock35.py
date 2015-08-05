#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
import knock30 as takayuki

def main():
    
    mecab_file = open(sys.argv[1], "r")
    all_sentences = takayuki.make_morphdicts(mecab_file)
    mecab_file.close()

    length_dict = dict()
    nounstring  = str()
    noun_count  = 0

    for one_sentence in all_sentences:
        for morphdict in one_sentence:
            if morphdict["pos"] == "名詞": 
               nounstring += morphdict["surface"]
               noun_count += 1
            else:
               length_dict[noun_count] = nounstring
               nounstring = str()
               noun_count = 0

    print length_dict[max(length_dict.keys())]


if __name__=="__main__":
   main()
