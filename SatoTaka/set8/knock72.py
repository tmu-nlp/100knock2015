#!/usr/bin/python
# _*_ coding:utf-8 _*_

from stemming.porter2 import stem
from knock71 import check_stopword

def main():
    sentiment_file = open("sentiment.txt")
    cleaned_list = list()
    for line in sentiment_file:
        words = line.strip().split(" ")
        for word in words[1:]:
            if not check_stopword(word):
               cleaned_list.append(stem(word))
        print words[0]+" "+" ".join(cleaned_list)
        cleaned_list = list()

    sentiment_file.close()

if __name__=="__main__":
   main()
