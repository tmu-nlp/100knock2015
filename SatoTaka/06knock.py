#!/usr/bin/python
# _*_ coding:utf-8 _*_

original_1 = "paraparaparadise"
original_2 = "paragraph"

ori_l_1 = list(original_1)
ori_l_2 = list(original_2)          #文字列をリスト化

bi_gram_1 = []
bi_gram_2 = []

for index in range(len(ori_l_1) - 1):
    my_list_1 = []
    for i in range(index, index+2):
        my_list_1.append(ori_l_1[i])
    bi_gram_1.append(tuple(my_list_1))

for index in range(len(ori_l_2) - 1):
    my_list_2 = []
    for j in range(index, index+2):
        my_list_2.append(ori_l_2[j])
    bi_gram_2.append(tuple(my_list_2))

X = set(bi_gram_1)
Y = set(bi_gram_2)

print X
print Y

### set は重複と順序を持たない要素の集合オブジェクト

wa = X.union(Y) #和集合
print wa

seki = X.intersection(Y) #積集合
print seki

sa = X.difference(Y) #差集合
print sa

if ("s", "e") in X:
   print 1
