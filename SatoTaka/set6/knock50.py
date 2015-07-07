#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys

def cut(nlp_file):
    sentences = list()
    for line in nlp_file:
        line = list(line.strip())
        for index in range(1,len(line)):
            if line[index].isupper():
               if line[index-1] == " " and line[index-2] in [".", ";", ":", "?", "!"]:
                  line[index-1] = "\n" 
        sentences.append("".join(line))
    return sentences


def main():
    nlp_file = open(sys.argv[1], "r")
    cut_sentence = cut(nlp_file)
    nlp_file.close()

    for sentence in cut_sentence:
        print sentence

if __name__=="__main__":
   main()
