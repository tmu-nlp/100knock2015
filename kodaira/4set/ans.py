import re

def jpline(line):  
  if len( line.replace('\t',',').split(',') ) > 4:
    return True
  else:
    return  False

class Morph:
  def __init__(self,line):
    self.surface = line.replace('\t',',').split(',')[0]
    self.base = line.replace('\t',',').split(',')[5]
    self.pos = line.replace('\t',',').split(',')[1]
    self.pos1 = line.replace('\t',',').split(',')[2]
  def mklist(self):
    return [self.surface,self.base,self.pos,self.pos1]
    
    
if __name__ == '__main__':
  #open the result text of (51)
  f = open("neko.txt.mecab","r") 
  lines = f.read()
  
  for line in lines:
    if jpline(line):
      morph = Morph(line)
      print line
      print morph.mklist()
