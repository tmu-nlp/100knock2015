#usr/bin/python
#coding:utf-8


import math
import pickle
from scipy.sparse import lil_matrix
from collections import defaultdict


def cal_ppmi(word,context):
    if word+' '+context not in word_cooccurrence_dict:
        return 0
    ppmi = max(math.log((N*word_cooccurrence_dict['%s %s' % (word,context)])/float(word_count_dict[word]*c_word_dict[context]),2),0)
    return ppmi


def main():
    t_set = set()
    c_set = set()
    for key,freq in word_cooccurrence_dict.items():
        if freq >= 10:
            t_set.add(key.split(' ')[0])
            c_set.add(key.split(' ')[1])
    matrix = lil_matrix((10000,10000))
    t_set = list(t_set)
    t_set.insert(0,'United_States')
    t_set.insert(0,'U.S')
    t_set.insert(0,'England')
    t_set.insert(0,'Spain')
    t_set.insert(0,'Madrid')
    t_set.insert(0,'Athens')
    for index,t in enumerate(t_set):
        if index == 10000:
            break
        for index_,c in enumerate(c_set):
            if index_ == 10000:
                break
            if cal_ppmi(t,c) != 0:
                matrix[index,index_] = cal_ppmi(t,c)
    pickle.dump([matrix,t_set],open('part84.dump','w'))
    print matrix.todense()[1]


if __name__ == '__main__':
    word_count_dict,c_word_dict,word_cooccurrence_dict,N = pickle.load(open('part83.dump'))
    main()
