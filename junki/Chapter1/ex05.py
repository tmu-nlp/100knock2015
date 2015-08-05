#!/usr/bin/python
#-*-coding:utf-8-*-

def ngramword(text, n):#ngram関数
    results = []#結果を格納
    if len(text) >= n:#テキストの長さが２以上のときループ開始
        for i in range(len(text)-n+1):
            results.append(text[i:i+n])#結果のリストにオブジェクトを追加
    return results

if __name__ == '__main__':
	text = 'I am an NLPer'
	list = str.split(text)
	
	for e in ngramword(text, 2):#関数呼び出し
		print e
	for e in ngramword(text.split(), 2):#区切った単語のリストを関数に渡す
		print e