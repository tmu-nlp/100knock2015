#!/usr/bin/python
# -*- coding:utf-8

#03. 円周率
#"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

if __name__ == "__main__":
    sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    pi = []

    for word in sent.split():
        if "," in word or "." in word:
            pi.append(len(word[:-1]))
        else:
            pi.append(len(word))

    print pi



