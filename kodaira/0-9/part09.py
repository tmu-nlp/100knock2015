#coding: UTF-8
#スペースで区切られた単語列に対して、各単語の先頭と末尾の文字は残し、
#それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ
#ただし、長さ４以下の単語は並び替えないものとする。
import random

# 5文字以上の文字列を先頭と最後尾を残し入れ替える
def wordsShuffle(words):
  shuffle = ""
  
  for word in words:
    #　４文字以上だったら混ぜて、そうでなかったら、そのまま追加
    if len(word) > 4:
      shuffle += word[0] + wordShuffle(word[1:-1]) + word[-1]
    else:
      shuffle += word
    # 空白を追加
    shuffle += ' '

  return shuffle

# 受け取った文字列を並び替える
def wordShuffle(word):
    
  # リストに変換
  word_list = list(word)
  # 入れ替える
  random.shuffle(word_list)
  # リストを文字列に直す
  shuffle = "".join(word_list)
  
  
  return shuffle

if __name__ == "__main__":
  sample = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
  words = sample.split(" ")
  print wordsShuffle(words)
