#!usr/bin/pythhon
# refarence: http://qiita.com/yubessy/items/1869ac2c66f4e76cd6c5
# website: http://nlp.stanford.edu/software/corenlp.shtml
#
# make xml: java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file input.txt


def get_content_tags(line, tag_name):
    return line.strip().replace("/", '').replace(tag_name, '')
 

def print_token(file_name):
    tag_word = "<word>"
    tag_sentence = "<sentence>"
    for line in open(file_name):
        if tag_word in line:
            print get_content_tags(line, tag_word)
        elif tag_sentence in line:
            ''
if __name__ == "__main__":
    file_name = "nlp.txt.xml"
    print_token(file_name)
