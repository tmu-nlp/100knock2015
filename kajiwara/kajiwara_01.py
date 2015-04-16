# coding:utf-8


def main(sentence):
    print "".join(list(sentence)[::2]).encode("utf-8")


if __name__ == '__main__':
    main(u"パタトクカシーー")
