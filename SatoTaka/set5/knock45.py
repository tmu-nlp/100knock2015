#!/usr/bin/python
# _*_ coding:utf-8 _*_ 

import sys
import knock41 as takayuki

def main():
    
    cabocha_file = open(sys.argv[1], "r")
    all_sentences = takayuki.make_chunks(cabocha_file)
    cabocha_file.close()

    particles = list()

    for chunks in all_sentences:
        for chunk in chunks:
            if chunk.check_pos("動詞") and chunk.srcs:
               particles = list()
               for departure in chunk.srcs:
                   if chunks[departure].check_pos("助詞"):
                      particles.append(chunks[departure].get_base_havingpos("助詞"))
               print chunk.get_phrase() + "\t" + " ".join(particles)


if __name__ == "__main__":
   main()
