#!usr/bin/python
#coding:utf-8


from gensim.models import word2vec
import pickle
import sys

def part86(model):
    print 'United_Statesのvec'
    print model['United_States']

def part87(model):
    print 'United_StatesとU.Sのcos_sim'
    print model.similarity('United_States','U.S')

def part88(model):
    print 'Englandのcos_sim'
    for word,similarity in model.most_similar(positive=['England']):
        print '%s : %f' % (word,similarity)

def part89(model):
    print 'vec(Spain)-vec(Madrid)+vec(Athens)'
    for word,similarity in model.most_similar(positive=['Spain','Athens'],negative=['Madrid']):
        print '%s : %f' % (word,similarity)


def main():
    model = word2vec.Word2Vec.load('matrix.model')
    if int(sys.argv[1]) == 86:
        part86(model)
    if int(sys.argv[1]) == 87:
        part87(model)
    if int(sys.argv[1]) == 88:
        part88(model)
    if int(sys.argv[1]) == 89:
        part89(model)

if __name__ == "__main__":
    main()
