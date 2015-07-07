# coding:utf-8
"""
python knock071.py
"""

import sys
import doctest
from nltk.corpus import stopwords

def is_stop(s):
    """
    >>> is_stop("a")
    True
    >>> is_stop("i")
    True
    >>> is_stop("stop")
    False
    """
    return s in stopwords.words('english')

if __name__ == "__main__":
    doctest.testmod()
