#coding: UTF-8
# 定型文を返す関数の作成
def info(x, y, z):
  return '%d時の%sは%.1f' % (x, y, z)

if __name__ == "__main__":
  x = 12
  y = '気温'
  z = 22.4
  print info(x, y, z)