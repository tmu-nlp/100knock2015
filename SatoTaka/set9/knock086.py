#!/usr/bin/python
# _*_ coding:utf-8 _*_

import pickle

def main():
    t_c_matrix = open("t_c_matrix", "r")
    t_set      = open("t_set", "r")

    word_context_matrix = pickle.load(t_c_matrix)
    word_set = pickle.load(t_set)
    word_set = list(word_set)

    word_index = word_set.index("United_States")

    print word_context_matrix[word_index]
#    for each in word_context_matrix[word_index]:
#        print each
#    print sum(word_context_matrix[word_index])

    t_c_matrix.close()
    t_set.close()

if __name__=="__main__":
   main()
