#!usr/bin/python
#--*--coding:utf-8--*--
from collections import defaultdict
class Morph(object):
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk(object):
    def __init__(self,morphs,dst,srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
    def get_phrase(self):
        phrase = ''
        for morph in self.morphs:
            phrase += morph.surface
        return phrase
    def get_pos(self):
        pos_list = list()
        for morph in self.morphs:
            pos_list.append(morph.pos)
        return pos_list
    def get_pos1(self):
        pos1_list = list()
        for morph in self.morphs:
            pos1_list.append(morph.pos1)
        return pos1_list
    def get_particles(self):
        particle_list = list()
        for morph in self.morphs:
            if morph.pos == '助詞':
                particle_list.append(morph.base)
        return particle_list
    def get_verb(self):
        verb = False
        for morph in self.morphs:
            if morph.pos == '動詞':
                verb = morph.base
                break
        if verb == '':
            return False
        elif verb:
            return verb



def make_chunk_list():
    chunk_list = []
    sent_list = []
    relate_dict = defaultdict(list)
    for line in open('neko.cabocha'):
        if line.startswith('*'):
            morphs = []
            relate_list = line.strip().split(' ')
            dst = int(relate_list[2][:-1])#係り先のDを消す
            chunk_list.append(Chunk(morphs,dst,relate_dict[int(relate_list[1])]))
            relate_dict[dst].append(int(relate_list[1]))
            
        elif '\t' in line:
            surf, item = line.strip().split('\t')
            items = item.split(',')
            morphs.append(Morph(surf,items[6],items[0],items[1]))
        elif 'EOS' in line:
            sent_list.append(chunk_list)
            chunk_list = []
            relate_dict = defaultdict(list)
    return sent_list
if __name__ == '__main__':
    sent_list = make_chunk_list()
    for chunk in sent_list[7]:
#        print '______',chunk.get_verb()
        print chunk.dst,chunk.srcs
        for  morph in chunk.morphs:
            print morph.surface
