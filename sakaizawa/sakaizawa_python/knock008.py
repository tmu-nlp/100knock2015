#!/usr/bin/python
# -*- coding:utf-8 -*-

#08. 暗号文
#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
#   英小文字ならば(219 - 文字コード)の文字に置換
#   その他の文字はそのまま出力
#
#この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(string):
    result = ''
    for char in string:
        if char.islower():
            result += chr(219 - ord(char))
        else:
            result += char
    return result

if __name__ == '__main__':
    s = 'Test Stringa'
    print s
    print '\nEncode'
    print cipher(s)
    print '\nDecode'
    print cipher(cipher(s))







