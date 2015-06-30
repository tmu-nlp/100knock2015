#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
import random

def main():
    positive_file  = open(sys.argv[1], "r")
    negative_file = open(sys.argv[2], "r")
    label = "+1 "
    sentiment_list = list()

    for posline in positive_file:
        posline = posline.strip()
        label += posline
        sentiment_list.append(label)
        label = "+1 "
        
    label = "-1 "
    for negline in negative_file:
        negline = negline.strip()
        label += negline
        sentiment_list.append(label)
        label = "-1 "

    random.shuffle(sentiment_list)

    for line in sentiment_list:
        print line

    positive_file.close()
    negative_file.close()


if __name__=="__main__":
   main()

