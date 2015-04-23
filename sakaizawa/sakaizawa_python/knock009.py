#!/usr/bin/python
# -*- coding:utf-8 -*-

#09. Typoglycemia
#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random

if __name__ == '__main__':
    sent = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    shuf_sent = list()
    for tok in sent.split():
        if len(tok) <= 4:
            shuf_sent.append(tok)
        else:
            head = tok[0]
            middle = list(tok[1:-1])
            tail = tok[-1]
            random.shuffle(middle)
            tok = '%s%s%s' % (head, ''.join(middle), tail)
            shuf_sent.append(tok)
    print ' '.join(shuf_sent)





