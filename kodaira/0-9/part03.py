#coding: UTF-8
#例文を単語ごとに分け（単語、文字数）のリストを作成

if __name__ == "__main__":
  
  sample = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
  
  #単語ごとに分解
  words = sample.split(" ")
  
  #.の除去
  words[-1] = words[-1].rstrip(".")

  pi = ""
  
  for i in words:
      #,は数えない
    word = i.rstrip(",")
    pi += str(len(word) )

  print pi[0] + '.' + pi[1:]


  
