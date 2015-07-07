#!usr/bin/python

import nltk
from part51 import *

def stemming(file_name):
    stemmer = nltk.stem.PorterStemmer()
    for word in separate_word(file_name).split("\n"):
        print word + "\t" + stemmer.stem(word)
    


if __name__ == "__main__":
    file_name = "nlp.txt"
    stemming(file_name)




