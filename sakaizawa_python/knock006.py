#!/usr/bin/python
# -*- coding:utf-8

#06. 集合
#"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ

from knock005 import n_gram

if __name__ == "__main__":
    sent1 = "paraparaparadise"
    sent2 = "paragraph"
    X = set(n_gram(sent1, 2))
    Y = set(n_gram(sent2, 2))

    print "X"
    print X
    print "Y"
    print Y
    print u"和集合(X ∪Y)"
    print set(list(X) + list(Y))
    print u"積集合(X ∩Y)"
    print X & Y
    print u"差集合(X - Y)"
    print X - Y
    print u"差集合(Y - X)"
    print Y - X
    


