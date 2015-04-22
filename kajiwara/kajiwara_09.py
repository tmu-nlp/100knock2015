# coding:utf-8

import random


def typoglycemia(sentence):
    word_list = [word for word in sentence.split()]
    for i in range(len(word_list)):
        if len(word_list[i]) <= 4:
            continue
        char_list = list(word_list[i][1:-1])
        random.shuffle(char_list)
        word_list[i] = word_list[i][0] + "".join(char_list) + word_list[i][-1]
    return " ".join(word_list)


def main():
    sentence = "I couldn't believe that I could actually understand " \
               "what I was reading : the phenomenal power of the human mind ."
    print "sentence:    ", sentence
    print "typoglycemia:", typoglycemia(sentence)


if __name__ == '__main__':
    main()
