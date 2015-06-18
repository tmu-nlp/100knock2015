#!/usr/bin/python
# _*_ coding:utf-8 _*_

import knock41 as takayuki
import sys

def main():
    
    cabocha_file  = open(sys.argv[1], "r")
    all_sentences = takayuki.make_chunks(cabocha_file)
    cabocha_file.close()

    for chunks in all_sentences:
        for chunk in chunks:
            print chunk.get_phrase() + "\t" + \
                  chunks[chunk.dst].get_phrase()
    

if __name__ == "__main__":
   main()
