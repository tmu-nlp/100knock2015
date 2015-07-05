#!usr/bin/python
#-*-coding:utf-8-*-

from part41 import*


def main():
    all_sent_list = make_chunk_list()
    for line in all_sent_list:
        for chunk in line:
            if chunk.srcs and '動詞' in chunk.get_pos():#morphs[0].pos == '動詞':
                verb = chunk.get_verb()#morphs[0].base
                strings = sorted([' '.join(line[src].get_particles()) for src in chunk.srcs if '助詞' in line[src].get_pos()])
                phrase = sorted([line[src].get_phrase() for src in chunk.srcs if '助詞' in line[src].get_pos()])
                if strings:
                    print '%s\t%s\t%s' % (verb,' '.join(strings),' '.join(phrase))


if __name__ == '__main__':
    main()
