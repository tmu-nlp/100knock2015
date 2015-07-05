#coding:utf-8

from part41 import *

def main():
    all_sent_list = make_chunk_list()
    for line in all_sent_list:
        for index,chunk in enumerate(line):
          if len(chunk.morphs) >= 2:
              if chunk.srcs and chunk.morphs[0].pos1 == 'サ変接続' and chunk.morphs[1].base == 'を' and '動詞' in line[chunk.dst].get_pos():
                verb = line[chunk.dst].get_verb()
                strings = sorted([' '.join(line[src].get_particles()) for src in line[chunk.dst].srcs if '助詞' in line[src].get_pos() and 'サ変接続' not in line[src].get_pos1()])
                phrase = sorted([line[src].get_phrase() for src in line[chunk.dst].srcs if '助詞' in line[src].get_pos() and 'サ変接続' not in line[src].get_pos1()])
                if strings:
                    print '%s%s%s\t%s\t%s' % (chunk.morphs[0].base,chunk.morphs[1].base,verb,' '.join(strings),' '.join(phrase))




if __name__ == '__main__':
    main()
