#!/usr/bin/python
# _*_ coding: utf-8 _*_

# 09. Typoglycemia

import random

def randommm(sentence):
    
    index = 0

    words_list = sentence.split(" ")
    for word in words_list:    # wordに入るのは文字列
        if len(word) > 4:     #各文字列の長さが4より大きい時
           suraisu = list(word[1:len(word)-1])  #頭文字と単語末を除いたリスト
           word = list(word) 
           for i in range(1, len(word)-1):
               word[i] = suraisu.pop(random.choice(range(len(suraisu))))
        words_list[index] = "".join(word)
        index += 1    
    return " ".join(words_list)


a = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind . "
print a
print randommm(a)
