#!/usr/bin/python
#_*_coding:utf-8_*_


def file_input():
    input_pos_file = open("rt-polaritydata/rt-polaritydata/rt-polarity.pos", "r")
    input_neg_file = open("rt-polaritydata/rt-polaritydata/rt-polarity.neg", "r")
    input_pos_file.close()
    input_neg_file.close()

    return input_pos_file, input_neg_file


def main():
    input_pos_file, input_neg_file = file_input()


if __name__ == "__main__":
    main()
