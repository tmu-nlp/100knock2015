# coding:utf-8


def main(sentence):
    print map(len, sentence.replace(",", "").replace(".", "").split())


if __name__ == '__main__':
    main("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")
