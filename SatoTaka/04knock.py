#!/usr/bin/python
# _*_ coding: utf-8 _*_

#元素記号

original = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Als Sign Peace Seburity Clause. Arthur King Can."

o_e_word = original.split()
print o_e_word

my_dict = {}

for index in range(len(o_e_word)):
    if index in [0,4,5,6,7,8,15,18]:
       my_dict[o_e_word[index][0:1]] = index+1
    else:
       my_dict[o_e_word[index][0:2]] = index+1

print my_dict
