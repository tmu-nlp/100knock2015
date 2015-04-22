#!/usr/bin/python
# _*_ coding: utf-8 _*_

#暗号文

def cipher(sentence):

    sentence.replace(" ","")
    s_list = list(sentence)

    for index in range(len(s_list)):
        if s_list[index].islower():
           s_list[index] = chr(219 - ord(s_list[index]))
    
    b =  "".join(s_list)
    return b

a = "thisisapen"    
print a
print cipher(a)
print cipher(cipher(a))
