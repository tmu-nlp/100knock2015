#!/usr/bin/python
# _*_ coding:utf-8 _*_

import pickle
from collections import defaultdict
from knock087 import cos_sim

def main():
    t_c_matrix = open("t_c_matrix", "r")
    t_set      = open("t_set", "r")
    word_dict  = defaultdict(float)

    word_context_matrix = pickle.load(t_c_matrix)
    word_set = pickle.load(t_set)
    word_set = list(word_set)

#    print word_set.index("Spain")
#    print word_set.index("England")
#    print word_set.index("Athens")
    
    vec1 = word_context_matrix[word_set.index("Spain")]
    vec2 = word_context_matrix[word_set.index("England")]
    vec3 = word_context_matrix[word_set.index("Athens")]
    vec  = vec1 - vec2 + vec3

    for index, word in enumerate(word_set):
        sim = cos_sim(word_context_matrix[index], vec)
        word_dict[word] = sim

    count = 0
    for word, sim in sorted(word_dict.items(), key = lambda x:-x[1]):
        print word + "\t" + str(sim)
        count += 1
        if count == 9:
           break

if __name__=="__main__":
   main()
