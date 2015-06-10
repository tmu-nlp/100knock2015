#!usr/bin/python
# cutout of the word


from part50 import *


def separate_word(file_name):
    return sentence_segment(file_name).replace("\n", "\n\n").replace(" ", "\n")



if __name__ == "__main__":
  file_name = "nlp.txt"
  print separate_word(file_name)
