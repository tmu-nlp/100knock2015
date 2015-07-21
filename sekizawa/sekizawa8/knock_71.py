#!usr/bin/python

import sys

def Stopword_Search(word):
    stop_list = ["a", "the", "they", "it", "and", "but"]
    if word in stop_list:
        return False
    else:
        return True


if __name__ == "__main__":
    sentence = sys.argv[1]

    words = sentence.strip().split(" ")

    for word in words:
        print Stopword_Search(word)


