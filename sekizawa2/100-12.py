#!/usr/bin/python
#coding: utf-8

if __name__ == "__main__":

    my_file = open("hightemp.txt", "r")

    f1 = open("col1.txt", "w")
    f2 = open("col2.txt", "w")
    for line in my_file:
        words = line.split("\t")
        f1.write(words[0])
        f1.write("\n")
        f2.write(words[1])
        f2.write("\n")

    f1.close()
    f2.close()

