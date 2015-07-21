#!usr/bin/python

import nltk

if __name__ == "__main__":
    input_file =  open("sentiment.txt", "r")
    output_file = open("feature.txt", "w")
    stop_file =   open("stop_list.txt", "r")
    for line in stop_file:
        stop_list = line.split(",")
    stemmer = nltk.PorterStemmer()

    for line in input_file:
        words = line.strip().split(" ")
        feature = words[0]
        output_file.write(feature)
        words.pop(0)
        for word in words:
            word = unicode(word, errors='ignore')
            if word not in stop_list:
                print word
                stem = stemmer.stem(word)
                output_file.write(" " + stem)
        output_file.write("\n")

    input_file.close()
    output_file.close()
    stop_file.close()
