# coding:utf-8


def main(word):
    print "".join(list(word)[::2]).encode("utf-8")


if __name__ == '__main__':
    main(u"パタトクカシーー")
