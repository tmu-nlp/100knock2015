#!usr/bin/python
#coding:utf-8

import random

def main():
    input_file = open("part81.txt")
    word_list = list()
    for line in input_file:
        word_list = line.strip().split()
        word_list.insert(0,'<s>')
        for index, word in enumerate(word_list):
            if index == 0:
                continue
            if index == len(word_list)-1:
                break
            elif index <= 5 and len(word_list)-index <= 5:
                if index <= len(word_list)-index:
                    window = random.randint(1,index)
                elif index >= len(word_list)-index:
                    window = random.randint(1,len(word_list)-index)
            elif index <= 5 and len(word_list)-index >= 5:
                window = random.randint(1,index)
            elif index >= 5 and len(word_list)-index <= 5:
                window = random.randint(1,len(word_list)-index)
            elif index >= 5 and len(word_list)-index >= 5:
                window = random.randint(1,5)
            c_list_high = word_list[index:index+window+1]
            c_list_low = word_list[index-window:index]
            c_list_low.extend(c_list_high)
            while word in c_list_low: c_list_low.remove(word)
            c = '\t'.join(c_list_low)
            print word+'\t'+c

if __name__ == '__main__':
    main()

