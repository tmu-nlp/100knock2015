#!/usr/bin/python
# _*_ coding:utf-8 _*_

from gensim.models import word2vec

def main():
    # 学習
    sentences = word2vec.Text8Corpus("output081_300000.txt")
    model = word2vec.Word2Vec(sentences, size=400)
    # モデルの保存と読み込み
    model.save("sample.model")
#    model = word2vec.Word2Vec.load("sample.model")
    # knock086
    print model["United_States"]   
    # knock087
    print model.similarity("United_States", "U.S")
    # knock088
    for x, y in model.most_similar(positive=["United_States"]):
        print x, y
    
if __name__=="__main__":
   main()
