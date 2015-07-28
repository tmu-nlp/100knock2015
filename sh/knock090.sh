# bash knock090.sh ../Data/result/knock081/python/clean.txt ../Data/result/knock090/python/vectors.bin

word2vec -train $1 -output $2 -cbow 0 -size 200 -window 5 -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 1

