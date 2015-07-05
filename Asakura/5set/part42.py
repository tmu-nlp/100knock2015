#!usr/bin/python
#--*--coding:utf-8--*--

from part41 import *
def main():
    all_sent_list = make_chunk_list()
    for line in all_sent_list:
        for chunk in line:
            if chunk.dst > 0:
                sent = ''
                for phrase in chunk.morphs:
                    sent += phrase.surface
                sent += '\t'
                for phrase2 in line[chunk.dst].morphs:
                    if phrase2.surface.endswith('。') or phrase2.surface.endswith(','):
                        sent += phrase2.surface[:-1]
                    else:
                        sent += phrase2.surface

                print sent


if __name__ == '__main__':
    main()

