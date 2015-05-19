from knock005 import *

if __name__ == '__main__':
    tok1 = "paraparaparadise"
    tok2 = "paragraph"
    X = set(sent2char_bigram(tok1))
    Y = set(sent2char_bigram(tok2))
    print 'X'
    print X

    print '\nY'
    print Y

    print '\nX cup Y'
    print set(list(X)+list(Y))

    print '\nX cap Y'
    print X & Y

    print '\nX - Y'
    print X - Y

    print '\nY - X'
    print Y - X
