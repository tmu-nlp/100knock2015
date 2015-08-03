#!usr/bin/python
#coding:utf-8

import pickle
from gensim.models import word2vec


def main():
    input_file = open('questions-words.txt')
    output_file = open('family.txt','w')
    flag = False
    for line in input_file:
        if ': family' in line:
            flag = True
            continue
        if ':' in line and ': family' not in line:
            flag = False
        if flag:
            output_file.write('%s\n'%line.strip())


if __name__ == '__main__':
    main()
