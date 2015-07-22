#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
import pickle
from collections import defaultdict

def main():
    input_file    = open(sys.argv[1], "r")
    pickle1       = open("count_t_and_c.txt", "w")
    pickle2       = open("count_t", "w")
    pickle3       = open("count_c", "w")
    count_t_and_c = dict()
    count_t       = defaultdict(int)
    count_c       = defaultdict(int)
    count_N       = 0



    for line in input_file:
        items    = line.strip().split("\t")
        word     = items[0]
        contexts = items[1:]

        count_t[word] += 1 # 単語tの出現回数
        if word not in count_t_and_c:
           count_t_and_c[word] = dict()
        
        for context in contexts:
            count_c[context] += 1
            count_N +=1
            if context not in count_t_and_c[word]:
               count_t_and_c[word][context] = 1
            else:
               count_t_and_c[word][context] += 1
        print count_t_and_c
        if count_N == 10000:
           exit()


#            count_t_and_c[word][context] += 1
#    pickle.dump(count_t_and_c, pickle1)
#    pickle.dump(count_t, pickle2)
#    pickle.dump(count_c, pickle3)


    input_file.close()
    pickle1.close()
    pickle2.close()
    pickle3.close()

if __name__=="__main__":
   main()
