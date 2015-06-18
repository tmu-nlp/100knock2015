#!/usr/bin/python
# _*_ coding:utf-8 _*_

#ちょっとだけまちがってるよ

import sys
import knock41 as takayuki

def main():
    
    cabocha_file = open(sys.argv[1], "r")
    all_sentences = takayuki.make_chunks(cabocha_file)
    cabocha_file.close()

    for chunks in all_sentences:
        for chunk in chunks:
            particles = list()
            phrases   = list()
            if chunk.check_pos1("サ変接続") and chunk.check_base("を") and \
               chunks[chunk.dst].check_pos("動詞") and chunk.dst != -1:
               for departure in chunks[chunk.dst].srcs[:len(chunks[chunk.dst].srcs)-1]:
                   if chunks[departure].check_pos("助詞"):
                      particles.append(chunks[departure].get_base_havingpos("助詞"))
                      phrases.append(chunks[departure].get_phrase())
               if particles and phrases:
                  print chunk.get_phrase()+chunks[chunk.dst].get_base_havingpos("動詞")\
                        + "\t"+" ".join(particles)\
                        + "\t" + " ".join(phrases)
                  particles = list()
                  phrases   = list()

               

if __name__ == "__main__":
   main()
