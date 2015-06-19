#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
from collections import defaultdict

def make_morphdicts(mecab_file):
    
    all_sentences = list()
    one_sentence  = list()
    morphdict = defaultdict(lambda: 0)

    for line in mecab_file:
        line = line.strip()
        if "\t" in line:
           items = line.split("\t")
           morphdict["surface"] = items[0]
           morphdict["base"]    = items[3]
           if "-" not in items[4]:
              morphdict["pos"]  = items[4]
           else:
              morphdict["pos"]  = items[4].split("-")[0]
              morphdict["pos1"] = items[4].split("-")[-1]
           one_sentence.append(morphdict)    # 形態素をリストにいれる
           morphdict = defaultdict(lambda: 0)# 形態素を初期化
        elif "EOS" in line:
           all_sentences.append(one_sentence) # 文の終わりごとにいれる
           one_sentence = list()             
    return all_sentences


def main():
    
    mecab_file     = open(sys.argv[1], "r")
    all_sentences  = make_morphdicts(mecab_file)
    mecab_file.close()

    for one_sentence in all_sentences:
        for morphdict in one_sentence:
            for each_kind, each_item in morphdict.items():
                print each_kind+"\t"+each_item
            print 
        print "End_of_Sentence" 


if __name__ == "__main__":
   main()
