#!usr/bin/python
#coding:utf-8


from gensim.models import word2vec
import pickle

data = word2vec.Text8Corpus('part81.txt')
model = word2vec.Word2Vec(data, size=200)


if __name__ == "__main__":
    model.save('matrix.model')
