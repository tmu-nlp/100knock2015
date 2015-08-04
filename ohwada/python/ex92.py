#!/usr/bin/python
# -*- coding:utf-8 -*-

from gensim.models import word2vec



def ex92(data, model):

    f_out = open("eval_instances_new.txt", "w")

    for line in data:
        line = line.strip()
        words = line.split(" ")        
        try:
            # 最も類似度が高い単語を得たいので、model.most_similar の 0番目を取る
            (most_sim_word, sim) = model.most_similar(positive=[words[1],words[2]],\
                                                      negative=[words[0]])[0]
            new_line = line + " " + most_sim_word + " " + str(sim) + "\n"
            f_out.write(new_line)
        except:
            pass


if __name__ == "__main__":
    model = word2vec.Word2Vec.load_word2vec_format("vectors.bin", binary=True)
    data = open("eval_instances.txt", "r").readlines()

    ex92(data, model)
    
