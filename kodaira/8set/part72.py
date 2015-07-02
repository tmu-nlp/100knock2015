#!/usr/bin/python
#coding:utf-8
# count neg_pos : cut -c 1-2 | sort | uniq -c

from collections import defaultdict
import nltk
from part71 import *
import re

def count_stem(file_name, stem_dict, stop_list, sentiment):
    stemmer = nltk.stem.PorterStemmer()
    c = 0
    for line in open(file_name):
        c += 1
        print c
        for word in line.strip().split():
            if not word in stop_list:
                print line
                print word, stemmer.stem(word.decode('utf-8'))
                stem_dict[stemmer.stem(word)] += sentiment


def feature_extraction(sentiment_name):
    stem_dict = defaultdict(int)
    stop_list = make_stop_list('rt-polarity.pos', 'rt-polarity.neg')
    features_dict = dict()
    word_id_dict = dict()
    id_num = 0
    word_list = list()
    for line in open(sentiment_name):
        line = line.strip().split()
        word_list = list()    
        for word in line[1:]:
            if not word in stop_list:
               word_list.append(word)
        features_dict[tuple(word_list)] = (line[0])
    
    return features_dict       

if __name__ == "__main__":
    senti_file_name = "sentiment.txt"
    
    features_dict = feature_extraction(senti_file_name)


    stemmer = nltk.stem.PorterStemmer()

    ''' print word : 1
    for words, polarity in features_dict.items():
        print polarity,
        for word in words:
            try:
                print (stemmer.stem(word) + ':1'),
            except:
                print (word + ':1'),
        print 
    '''


# print unigram
    count_dict = defaultdict(float)
    count = 0
    for words, polarity in features_dict.items():
        for word in words:
            count += 1
            try:
                count_dict[stemmer.stem(word)] += int(polarity)
            except:
                count_dict[word] += int(polarity)

    for word in count_dict.keys():
        count_dict[word] /= float(count)
        if count_dict[word] == 0.0:
            count_dict[word] = 1 / float(count)

    for words, polarity in features_dict.items():
        print polarity,
        for word in words:
            try:
                word = stemmer.stem(word)
            except:
                word = word
            print (word + ':' + str(count_dict[word])),
        print 

