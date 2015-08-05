#!/usr/bin/python
# -*- coding:utf-8 -*-

import pickle
import numpy as np
from ex86 import output_vector
from ex88 import similar_top10


if __name__ == "__main__":
    vector1 = output_vector("Spain")
    vector2 = output_vector("Madrid")
    vector3 = output_vector("Athens")
    new_vector = vector1 - vector2 + vector3

    top10_lst = similar_top10(new_vector)
    for word, vec in top10_lst:
        print word, vec
