#!/usr/bin/python
#-*-coding:utf-8-*-

#paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def ngramword(text, n):#ngram関数
    results = []#結果を格納
    if len(text) >= n:#テキストの長さが２以上のときループ開始
        for i in range(len(text)-n+1):
            results.append(text[i:i+n])#結果のリストにオブジェクトを追加(スライスして結果に追加)
    return results

if __name__ == '__main__':
	text1 = 'paraparaparadise'
	text2 = 'paragraph'
	list1 = ngramword(text1, 2)#関数の呼び出しで引数としてparaparaparadiseと２を渡す
	list2 = ngramword(text2, 2)
	
	for e in list1:#関数呼び出し
		print e
	print '\n'
	for e in list2:
		print e
	
	a = set(list1)#setで集合にする
	b = set(list2)
	
	print "和集合%s" % (a | b)
	print "積集合%s" % (a & b)
	print "差集合%s" % (a - b)
	print "差集合%s" % (b - a)
	
