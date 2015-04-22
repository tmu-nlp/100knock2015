#!/usr/bin/python
# -*- coding:utf-8 -*- 

#02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

if __name__ == "__main__":
    tok = ""
    tok1 = u"パトカー"
    tok2 = u"タクシー"

    for i in range(len(tok1)):
        tok += tok1[i]
        tok += tok2[i]

    print tok

