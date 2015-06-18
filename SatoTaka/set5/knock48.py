#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
import knock41 as takayuki

def main():

    cabocha_file = open(sys.argv[1], "r")
    all_sentences = takayuki.make_chunks(cabocha_file)
    cabocha_file.close()

    for chunks in all_sentences:
        for chunk in chunks:
            phrases = list()
            if chunk.check_pos("名詞"):
               phrases.append(chunk.get_phrase())
               dst = chunk.dst
               while dst != -1:
                 phrases.append(chunks[dst].get_phrase())
                 dst = chunks[dst].dst
            if len(phrases) >= 2:
               print "->".join(phrases)
            

if __name__=="__main__":
   main()
