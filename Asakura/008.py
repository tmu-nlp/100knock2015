#!usr/bin/python
#--*--coding:utf-8--*--
import sys
import string

def cipher(mystr):
  array=[]
  for char in mystr:
    if char.islower():
      array.append(chr(219-ord(char)))
    else:
      array.append(char)
  mystring2= string.join(array,"")
  return mystring2

def cipher2(mystr):
  array=""
  for char in mystr:
    if char.islower():
      array += chr(219-ord(char))
    else:
      array += char
  return array


if __name__ == "__main__":
  mystring=sys.argv[1]
  print cipher(mystring)
  print cipher2(cipher(mystring))

