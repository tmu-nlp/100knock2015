#!usr/bin/python
#coding:utf-8

from collections import defaultdict

import nltk

if __name__ == "__main__":
    model_file = open("knock_73.model", "r")
    sentence = "an ideal love story for those intolerant of the more common saccharine genre ."
    weight_dict = defaultdict(lambda: 0)
    stemmer = nltk.PorterStemmer()
    score = 0.0

    for line in model_file:
        if "@" not in line:
            print line
            weight, stem = line.strip().split("\t")
            if type(weight) != float:
                if stem == "__BIAS__":
                    bias = weight
                else:
                    weight_dict[stem] = float(weight)

    words = sentence.split(" ")
    for word in words:
        stem = stemmer.stem(word)
        score += weight_dict[stem]

    print score
    if score < 0:
        print "-1"
    else:
        print "+1"


