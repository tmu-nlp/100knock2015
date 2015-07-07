#!/usr/bin/python
#-*-coding:utf-8-*-

#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#英小文字ならば(219 - 文字コード)の文字に置換。その他の文字はそのまま出力。
#この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(sentence):
	result = ''
	for char in sentence:
		if char.islower():#小文字ならば(islower()で小文字かどうか調べることができる)
			result += chr(219 - ord(char))#コードポイント変換をordでを行いresultに格納
		else :
			result += char#その他は標準で格納する
	return result

if __name__ == '__main__':
	givensentence = 'KomachiLab'
	print cipher(givensentence)