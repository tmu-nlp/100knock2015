#!usr/bin/python

import pickle
from collections import Counter
pairs = open('pair.txt', 'r')

co_occur_count = Counter()
cont_count = Counter()
word_count = Counter()
count = 0
for line in pairs:
    line = line.strip().split('\t')
    word = line[0]; cont_words = line[1:]
    word_count[word] += 1
    for cont_word in cont_words:
        count += 1
        cont_count[cont_word] += 1
        co_occur_count[word + '\t' + cont_word] += 1

print count
pickle.dump(dict(cont_count), open('cont.pkl', 'w') )
pickle.dump(dict(word_count), open('word.pkl', 'w') )
pickle.dump(dict(co_occur_count), open('co_occur.pkl', 'w') )
