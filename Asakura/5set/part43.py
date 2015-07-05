#!usr/bin/python
#-*-coding:utf-8-*-

from part41 import *

def main():
    all_sentence_list = make_chunk_list()

#    for line in all_sentence_list:
#        for chunk in line:
#            pos_list = chunk.get_pos()
#            for pos in pos_list:
#                print pos
    for line in all_sentence_list:
        for chunk in line:
            if int(chunk.dst) != -1:
                pos_list = chunk.get_pos()
                pos_list2 = line[int(chunk.dst)].get_pos()
                if '名詞' in pos_list and '動詞' in pos_list2:           
                    sentence1 = chunk.get_phrase()
                    sentence2 = line[int(chunk.dst)].get_phrase()
                    print sentence1+'\t'+sentence2

if __name__ == '__main__':
    main()
