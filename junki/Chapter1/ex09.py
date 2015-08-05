#!/usr/bin/python
#-*-coding:utf-8-*-

#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random

if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    shuf = list()
    for word in sentence.split():
        if len(word) <= 4:#単語が４語以下のときそのままwordに加える
            shuf.append(word)
        else:#４文字以上のとき
            first = word[0]#wordの中の１文字目添え字０番目
            mid = list(word[1:-1])#４文字以上のwordのなかで最初と最後以外のアルファベットをスライスで抽出
            last = word[-1]#最後から数えて初めのもの
            random.shuffle(mid)#pythonの標準のランダム関数を呼び出し中間(mid)をシャッフルする
            word = '%s%s%s' % (first, ''.join(mid), last)#シャッフルしたものを新たなwordに書き換える
            shuf.append(word)#シャッフルしたものをwordに加える
    print "\n"     
    print ' '.join(shuf)#空白を挟んで結合する
    print "\n"