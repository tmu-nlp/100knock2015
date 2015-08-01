#!usr/bin/python
#coding:utf-8

from collections import defaultdict
import pickle
def main():
    word_count_dict = defaultdict(lambda:0)
    c_word_dict = defaultdict(lambda:0)
    word_cooccurrence_dict = defaultdict(lambda:0)
    input_file = open('part82.txt')
    N = 0
    for line in input_file:
        word_list = line.strip().split('\t')
        word_count_dict[word_list[0]] += 1#f(t,∗): 単語tの出現回数
        for word in word_list[1:]:
            c_word_dict[word] += 1#f(∗,c): 文脈語cの出現回数
            word_cooccurrence_dict[word_list[0]+' '+word] += 1#f(t,c): 単語tと文脈語cの共起回数
            N += 1

    f = open('part83.dump','w')
    pickle.dump([dict(word_count_dict),dict(c_word_dict),dict(word_cooccurrence_dict),N],f)
    f.close()
if __name__ == '__main__':
    main()
