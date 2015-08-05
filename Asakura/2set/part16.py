#!isr/bin/python
#--*--coding:utf-8--*--

import sys

if __name__ == "__main__":
  infile = open(sys.argv[1],"r")
  N = int(sys.argv[2])
  count = 0
  mylist=[]
  array=[]
  for line in infile:
      count +=1
      array.append(line)
  for num in range(0,N):
      setnum =float(count)/N
      if setnum > (count/N):
         mylist.append(count/N + 1)
         count -=(int(setnum)+1)
      if setnum <= (count/N):
         mylist.append(count/N)
         count -=(int(setnum))
      if count <= (count/N):
         break;
      N -= 1
     # count -= (int(setnum)+1)
  print mylist
  f = open("016.txt","w")
  i=0
  for index in mylist :
      for index in range(0,int(index)):
          f.write(array[i])
          i+=1
      f.write("\n")   
  f.close()
