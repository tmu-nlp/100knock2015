#!/bin/sh

WORD2VEC=/work/owada/word2vec/trunk/word2vec

# set9 の 81. で作成したコーパス(corpus.txt) に対する word2vec の適用結果を vectors.bin に保存
time $WORD2VEC -train ../set9/corpus.txt -output vectors.bin -cbow 1 -size 200 -window 8 -negative 25 -hs 1 -sample 1e-3 -threads 20 -binary 1
