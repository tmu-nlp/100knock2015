#coding: UTF-8
# 二つの単語からそれぞれの文字バイグラムの集合を生成し、それらの和、積、差集合を求める
# 'se'というバイグラムがそれぞれの集合に含まれているか確かめる


def makeUnion(list1, list2) :
  union = list()
  for i in list1:
    if not i in union:
      union.append(i)
  for i in list2:
    if not i in union:
        union.append(i)
  return union

def makeIntersection(list1, list2):
  intersection = list()
  for i in list1:
    if not i in list2 and not i in intersection:
      intersection.append(i)
  return intersection

if __name__ == "__main__":
  from part05 import *
  
  sample1 = 'paraparaparadadise'
  sample2 = 'paragraph'
 
  X = makeBigram(list(sample1) )
  Y = makeBigram(list(sample2) )

#  print '集合X　＝',;   print X
#  print '集合Y　＝',;   print Y
#  print makeUnion(X, Y)
#  print makeIntersection(X, Y)

#関数を作れとは書いてなかった
  print X
  X = set(X)
  Y = set(Y)
  print X
  se = ('s', 'e')
  #和集合
  union = X | Y
  #積集合
  intersection = Y & X
  #差集合
  set_differenceXY = X - Y
  set_differenceYX = Y - X

  print '和集合：'; print union
  print '積集合：'; print intersection
  print '差集合（X-Y）'; print set_differenceXY
  print '差集合（Y-X）'; print set_differenceYX
  
  if se in X:
    print 'Xにはseが含まれている'
  if se in Y:
    print 'Yにはseが含まれている'