#!usr/bin/python
#coding:utf-8


import pickle 
def main():
    matrix,t_set = pickle.load(open('part85.dump'))
    word_index = list(t_set).index('United_States')
    print word_index
    print matrix[word_index]

if __name__ == '__main__':
    main()
