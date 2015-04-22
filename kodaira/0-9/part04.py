#coding: UTF-8
#単語の先頭1､2文字を取り出す。

if __name__ == "__main__":
    
  sample = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause Arthur King Can"
  
  from collections import OrderedDict
  dict = OrderedDict()
  
  numbers = [1, 5, 6, 7, 8, 9, 15, 16, 19]
  num = 0
  
  words = sample.split(" ")
  
  for i in words:
      #文字を取り出す　ついでに番号振って辞書つくる
    x = 1
    if num + 1 in numbers:
      x = 0
    #先頭から１or２文字拾ってくる
    dict[i[: 1 + x] ] = num + 1
    num += 1
  
  for foo, bar in dict.items():
    print 'element:%2s , number: %2d' % (foo, bar)