#coding: UTF-8
# 例文から単語bi-gram文字bigramを得よ

from collections import OrderedDict

# リストを受け取りバイグラムにする。
def makeBigram(words):
  Word = list()
  words.insert(0, "<s>")
  words.append("</s>")
  
  #　二つずつとってリストに
  for i in range(0, len(words) - 2 + 1):
    Word.append((words[i], words[i + 1]) )
  
  return Word

# リストを受け取りnグラムにする
def makeNgram(words, n):
  if n < 1 or len(words) < n :
    print '１以下の入力'
    return words;
  WordList = list()
  for i in range(0, len(words) - n + 1):
    word = ""
    word += '('
    for j in range(0, n):
      word += '\'' + words[j + i] + '\''
      if not j == n - 1:
        word += ', '
    word += ')'
    WordList.append(word)
  #　nずつとってリストに
  return WordList


if __name__ == "__main__":
  sample = "NLPer"
  #print 'words bigram:'
  #print makeBigram(sample.split(" ") )
  #print 'charactor bigram:'
  print makeNgram(list(sample), 5)