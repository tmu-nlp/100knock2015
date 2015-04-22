#coding: UTF-8
# 以下の使用で文字列を変換する関数cipherを実装せよ
# ・英小文字ならば（219ー文字コード）の文字に置換
# ・他の文字はそのまま出力
# 暗号化し、復号化する。
# つまり、aをz　zをaに変換するものを作れ（a = 97, z = 122）
# これを作れば、復号化も暗号化もできると

# a-z反転する関数
def cipher(words):
  w = ''
  for i in words:
    # islower 小文字を含み　かつ　大文字を含まないものをtrueとする
    if i.islower():
      # chr() 数値を文字コードに変換、ord()　文字を数値に変換
      w += chr(219 - ord(i) )
    else:
      w += i
  return w
            
            

if __name__ == '__main__':
  sample = 'Hi He Lied Because Boron Could Not Oxidize Fluorine.'
  cip = cipher(sample)
  print cip
  dec = cipher(cip)
  print dec