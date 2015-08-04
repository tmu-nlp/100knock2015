#!/usr/bin/python
# -*- coding:utf-8 -*-

from gensim.models import word2vec


model = word2vec.Word2Vec.load_word2vec_format("vectors.bin", binary=True)

# ex86
print "ex86"
print "The vector of 'United_States'"
print model["United_States"]
print ""

# ex87
print "ex87"
print "The cosine simirality between the vectors of 'United_States' and 'U.S'"
print model.similarity("United_States", "U.S")
print ""

# ex88
print "ex88"
print "Top10 most similar words and theirs vectors of 'England'"
for vec, sim in model.most_similar(positive="England"):
    print vec, sim
print ""

# ex89
print "ex89"
print "The vector of 'Spain - Madrid + Athens'"
print model["Spain"] - model["Madrid"] + model["Athens"]
print ""
print "Top10 most similar words and theirs vectors of above vector"
for vec, sim in model.most_similar(positive=["Spain", "Athens"], negative=["Madrid"]):
    print vec, sim
