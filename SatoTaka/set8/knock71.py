#!/usr/bin/python
# _*_ coding:utf-8 _*_ 

def check_stopword(word):
    stopwords = open("stop_word.txt")
    stopwords_list = [stopword.strip() for stopword in stopwords]

    if word in stopwords_list: 
       return True
    else:
       return False
    stopwords.close()

def main():

    sentiment_list = open("sentiment.txt")
    stopwords      = open("stop_word.txt")

    for line in sentiment_list:
        words = line.split(" ")[1:]
        for word in words:
#            print word
            check_stopword(word)

    sentiment_list.close()
    stopwords.close()
    

if __name__=="__main__":
   main()
