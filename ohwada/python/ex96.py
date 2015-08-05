#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from gensim.models import word2vec
from ex81 import make_country_name_lst


def extr_country(model):
    # ex81 で用いた国名リストを作る関数
    country_lst = make_country_name_lst()
    vec_lst = []
    for country in country_lst:
        country = "_".join(country.strip().split(" "))
        try:
            print country
            print model[country]
            vec_lst.append(model[country])
        except:
            pass

    np.save("country_vectors", vec_lst)


if __name__ == "__main__":
    model = word2vec.Word2Vec.load_word2vec_format("vectors.bin", binary=True)
    extr_country(model)
