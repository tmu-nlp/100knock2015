# coding:utf-8

import kajiwara_05 as get_n_gram


def char_n_gram_set(word, n):
    n_gram_set = set()
    [n_gram_set.add("".join(n_gram)) for n_gram in get_n_gram.char_n_gram(word, n)]
    return n_gram_set


def sum_set(set1, set2):
    return set1 | set2


def product_set(set1, set2):
    return set1 & set2


def difference_set(set1, set2):
    return set1 - set2


def is_involved(token, n_gram_set):
    if token in n_gram_set:
        return True
    return False


def main():
    X = char_n_gram_set("paraparaparadise", 2)
    Y = char_n_gram_set("paragraph", 2)
    print "X:", X
    print "Y:", Y
    print "sum_set(X, Y):", sum_set(X, Y)
    print "product_set(X, Y):", product_set(X, Y)
    print "difference_set(X, Y)", difference_set(X, Y)
    print "is_involved('se', X)", is_involved("se", X)
    print "is_involved('se', Y)", is_involved("se", Y)


if __name__ == '__main__':
    main()
