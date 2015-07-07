#!usr/bin/python

import nltk

if __name__ == "__main__":
    input_file  = open("output_51.txt", "r")

    stemmer = nltk.PorterStemmer()
    for term in input_file:
        stem = stemmer.stem(term.strip())
        print term.strip() + "\t" + stem

    input_file.close()

