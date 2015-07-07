#coding:utf-8


from part41 import *


def main():
    all_sent_list = make_chunk_list()
    for sent in all_sent_list:
        for chunk in sent:
            if chunk.srcs and '動詞' in chunk.get_pos():#chunk.morphs[0].pos == '動詞':
                verb = chunk.get_verb()#morphs[0].base
                strings = sorted([' '.join(sent[src].get_particles()) for src in chunk.srcs if '助詞' in sent[src].get_pos()])
                if strings:
                    print '%s\t%s' % (verb,' '.join(strings))



if __name__ == '__main__':
    main()

