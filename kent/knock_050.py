#!/usr/bin/python
#_*_coding:utf-8_*_


def split():

    for line in open("nlp.txt", "r"):
        line = list(line.strip())

        for index in range(1, len(line)):
            if line[index].isupper():
                if line[index - 1] == " ":
                    if line[index - 2] in [".", ";", ":", "?", "!"]:
                        #print line[index - 2] + line[index - 1] + line[index]
                        #line[index - 1] = line[index - 1].replace(" ", "\n")
                        line[index - 1] = "\n"
        print "".join(line)


if __name__ == "__main__":

    #input_file = open("nlp.txt", "r")
    split()
