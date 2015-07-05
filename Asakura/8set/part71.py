#!usr/bin/python
#coding:utf-8

import sys

def make_stop_word():
    stop_list_file = open('stopwordlist')
    stop_word_list = list()
    for line in stop_list_file:
        line_list = line.strip().split()
        for stop_word in line_list:
            stop_word_list.append(stop_word)


    return stop_word_list
def check_stop_word(stop_word_list,word):
    if word in stop_word_list:
        return True
    else:
        return False

if __name__ == '__main__':
    stop_word_list = make_stop_word()
    print check_stop_word(stop_word_list,sys.argv[1])
