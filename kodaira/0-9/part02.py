#coding: UTF-8
#文字列の連結

if __name__ == "__main__":
  sample1 = u"パトカー"
  sample2 = u"タクシー"
  ans = u""

  for i in range(0, len(sample1) ):
    ans += sample1[i] + sample2[i]

  print ans