#!usr/bin/python
#coding:utf-8

from part41 import *


def main():
    all_sent_list = make_chunk_list()
    for line in all_sent_list:
        for index,chunk in enumerate(line):
            if '名詞' in chunk.get_pos() and chunk.dst > 0:
                print line[index].get_phrase(),
                while line[index].dst > 0:
                    print '->',
                    print line[line[index].dst].get_phrase(),
                    index = line[index].dst
                print ''


if __name__=='__main__':
    main()
