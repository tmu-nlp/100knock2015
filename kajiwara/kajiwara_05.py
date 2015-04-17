# coding:utf-8


def n_gram(token_list, n):
    return [token_list[i:i+n] for i in range(len(token_list)-(n-1))]


def word_n_gram(sentence, n):
    print n_gram(sentence.split(), n)


def char_n_gram(sentence, n):
    print n_gram(list(sentence.replace(" ", "")), n)


def main():
    word_n_gram("I am an NLPer", 2)
    char_n_gram("I am an NLPer", 2)


if __name__ == '__main__':
    main()
