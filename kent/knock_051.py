#!/usr/bin/python
#_*_coding:utf-8_*_


def split_function(file_50):
#ダメなやつ。ピリオドや？が来たときに改行されない
    for line in file_50:
        words = line.strip().split(" ")
        for word in words:
            if "." in word:
                print word
                print
            else:
                print word


def fixed_split(file_50):

    for line in file_50:
        word = line.split(" ")
        print "\n".join(word)

if __name__ == "__main__":

    file_50 = open("file_50.txt", "r")
    fixed_split(file_50)
