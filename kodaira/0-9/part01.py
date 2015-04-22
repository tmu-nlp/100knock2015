#coding: UTF-8
# スライスを使って文字を取り出す + unicode を使う
if __name__ == "__main__":
    
  # unicodeで代入
  sample = u"パタトクカシーー"
  
  # スライス1個飛ばし
  ans = sample[::2]
  
  print ans

  ans = sample[1::2]

  print ans