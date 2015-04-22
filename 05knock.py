#!/usr/bin/python
# _*_ coding: utf-8 _*_
def n_gram(sentence, n):

    e_w_list = sentence.split(" ")

    word_n_gram = []

    for index in range(len(e_w_list)-n+1):
        my_list = []
	for i in range(index, index+n):
            my_list.append(e_w_list[i])
        word_n_gram.append(tuple(my_list))
    print word_n_gram


    char_n_gram = []

    e_c_list = sentence.split(" ")
    e_c_c = "".join(e_c_list)
    e_c_list = list(e_c_c)

    for index in range(len(e_c_list)-n+1):
        my_list = []
        for i in range(index, index+n):
            my_list.append(e_c_list[i])
        char_n_gram.append(tuple(my_list))
    print char_n_gram
n_gram("I am an NLPer", 3)
