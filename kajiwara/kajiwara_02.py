# coding:utf-8


def main(word1, word2):
    print "".join([char1+char2 for char1, char2 in zip(list(word1), list(word2))]).encode("utf-8")


if __name__ == '__main__':
    main(u"パトカー", u"タクシー")
