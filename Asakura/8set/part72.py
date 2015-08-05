#!usr/bin/python
#coding;utf-8

from stemming.porter2 import stem
from part71 import *

def main():
    input_file = open('sentiment.txt')
    stop_word_list = make_stop_word()
#    feature_list = list()
    sentence_feature_list = list()
    for line in input_file:
        input_list = line.strip().split()
        label = input_list[0]
        for word in input_list:
            word = word.lower()
            if word not in stop_word_list and len(word) > 3 :
#                feature_list.append(stem(word))
                sentence_feature_list.append(stem(word))
        print label+" "+ " ".join(sentence_feature_list)
        sentence_feature_list = []
#    feature_list = list(set(feature_list))


if __name__ == '__main__':
    main()
