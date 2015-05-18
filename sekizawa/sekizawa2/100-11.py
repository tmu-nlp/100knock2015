#!/usr/bin/python
#coding: utf-8

if __name__ == "__main__":

    my_file = open("hightemp.txt", "r")

    for line in my_file:
        line.replace("\t", " ")
        print line,


