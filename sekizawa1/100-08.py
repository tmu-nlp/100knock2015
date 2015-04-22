#!/usr/bin/python
#coding: utf-8

def cipher(message):
    code = ""
    for i in range(len(message)):
        if 'a' <= message[i] <= 'z':
            code = code + chr(219 - ord(message[i]))
        else:
            code = code + message[i]

    return code

if __name__ == "__main__":
    sentence = "Natural Language Processing"
    encode =  cipher(sentence)
    print "暗号化：%s" % encode
    decode = ""
    for i in range(len(encode)):
        if 'a' <= chr(219 - ord(encode[i])) <= 'z':
            decode = decode + chr(219 - ord(encode[i]))
        else:
            decode = decode + encode[i]
    print "復号化：%s" % decode



