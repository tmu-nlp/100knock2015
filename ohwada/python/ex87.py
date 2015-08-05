#!/usr/bin/python
# -*- coding:utf-8 -*-

import pickle
import numpy as np
from ex86 import output_vector


def cos_simmilarity(vector_a, vector_b):
    len_a = np.linalg.norm(vector_a)
    len_b = np.linalg.norm(vector_b)    
    inner_pd = np.dot(vector_a, vector_b)
    print len_a, len_b, inner_pd
    cos_sim = inner_pd / (len_a * len_b)

    return cos_sim


if __name__ == "__main__":
    vector = output_vector("United_States")
    ano_vector = output_vector("U.S")
    cos_sim = cos_simmilarity(vector, ano_vector)
    print cos_sim
